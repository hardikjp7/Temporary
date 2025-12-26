#ifndef mainwindow_H
#define mainwindow_H

#include <QMainWindow>
#include <QVector>
#include <QMap>
#include <QString>
#include <QDateTime>

#include <QSplitter>
#include <QScrollArea>
#include <QScrollBar>
#include <QListWidget>
#include <QDateTimeEdit>
#include <QLineEdit>
#include <QCheckBox>
#include <QRadioButton>
#include <QPushButton>
#include <QTabWidget>
#include <QLabel>
#include <QSlider>
#include <QGroupBox>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QFormLayout>
#include <QFileDialog>
#include <QFile>
#include <QTextStream>
#include <QStandardPaths>
#include <QStyleFactory>
#include <QPalette>
#include <QComboBox>
#include <QSpinBox>
#include <QDataStream>
#include <QTimer>
#include <QElapsedTimer>

#include <QtCharts/QChartView>
#include <QtCharts/QChart>
#include <QtCharts/QLineSeries>
#include <QtCharts/QValueAxis>
#include <QtCharts/QDateTimeAxis>

#include <random>


namespace Ui {
class mainwindow;
}


QT_CHARTS_USE_NAMESPACE


//class mainwindow : public QMainWindow
//{
//    Q_OBJECT

//public:
//    explicit mainwindow(QWidget *parent = nullptr);
//    ~mainwindow();

//private:
//    Ui::mainwindow *ui;
//};

//#endif // mainwindow_H

struct DataRow {
    quint32 index;
    quint64 timestamp;
    quint8 cycleValue;  // New column for values 1-8
    double signalValues[80];
};

// Memory-efficient real-time data point structure
struct RealtimePoint {
    qint64 timestamp;  // milliseconds since epoch
    float value;       // using float instead of double to save memory

    RealtimePoint() : timestamp(0), value(0.0f) {}
    RealtimePoint(qint64 ts, float val) : timestamp(ts), value(val) {}
};

class mainwindow : public QMainWindow {
    Q_OBJECT
public:
    explicit mainwindow(QWidget *parent = nullptr);
    ~mainwindow();

    // Method to get the main widget for tab integration
//    QWidget* getMainWidget() { return centralWidget(); }

private slots:
    void onApply();
    void onReset();
    void onHideShowLeft();     // toggles left pane from left button
    void onShowLeftFromRight();// shows left pane from right button
    void onZoomChanged(int value);
    void onZoomChanged2(int value);
    void onHScrollChanged(int value);
    void onMarkersToggled(bool checked);
    void onThemeToggled(bool checked);
    void onExportPNG();
    void onExportCSV();
    void onTimeUnitChanged(int index);
    void onTimeUnitChanged2(int index);
    void onTimeValueChanged(int value);
    void onTimeValueChanged2(int value);
    void onSelectFile();  // New: File selection

    // sync external vertical scrollbar with left scroll area
    void onLeftExternalVScrollChanged(int v);
    void onLeftInternalVScrollChanged(int v);

    // Real-time plotting slots
    void onToggleRealtime(bool enabled);
    void onRealtimeTimerTimeout();
    void onRealtimeIntervalChanged(int value);
    void onRealtimeZoomChanged(int value);
    void onRealtimeScrollChanged(int value);
    void onRealtimeMemoryLimitChanged(int index);

    // Parameter search slots
    void onSearchTextChanged(const QString &text);
    void onDeselectAllClicked();

private:
    Ui::mainwindow *ui;

    // Data
    QStringList parameterNames;                 // "Signal_1" .. "Signal_80"
    QStringList allParameterNames;              // Store all parameter names for filtering
    QVector<QDateTime> timestamps;              // Timestamps from file
    QVector<quint8> cycleValues;                // New: Cycle values from file
    QMap<QString, QVector<float>> dataByParam;  // param -> values
    int totalSeconds = 0;
    QString currentDataFile;                    // Current loaded file

    // Memory mapping
    QFile *memoryMappedFile = nullptr;
    uchar *fileData = nullptr;
    qint64 fileSize = 0;
    bool usingMemoryMapping = false;

    // Windowing state
    int currentWindowSeconds = 0;    // size of visible window in seconds
    int currentWindowStartIdx = 0;   // start index in timestamps
    QStringList currentSelectedParams;

    // Chart containers
    QChart      *singleChart = nullptr;
    QChartView  *singleChartView = nullptr;
    QTabWidget  *tabWidget = nullptr;

    // Vertical lines for mode transitions
    QVector<QLineSeries*> modeTransitionLines;
    void addModeTransitionLines(QChart*chart, int i0, int i1);
    void clearModeTransitionLines();

    // Plotting params
    int maxPointsPerSeries = 10000; // downsampling cap

    // Real-time plotting members
    QTimer* m_realtimeTimer = nullptr;
    bool m_isRealtimePlotting = false;
    QMap<QString, QVector<RealtimePoint>> m_realtimeData; // Using memory-efficient structure
    std::default_random_engine m_randomGenerator;
    std::uniform_real_distribution<double> m_randomDistribution;
    QElapsedTimer m_realtimeElapsedTimer;
    qint64 m_realtimeStartTime = 0;

    // Real-time window control
    int m_realtimeWindowMinutes = 120;  // Default 2 hours window
    int m_realtimeScrollPosition = 0;    // 0 = show latest, max = show oldest

    // Memory limits
    int m_maxRealtimePointsPerParam = 72000; // 2 hours at 100ms (default)
    const qint64 TWO_HOURS_MS = 2 * 60 * 60 * 1000;
    const int DEFAULT_REALTIME_INTERVAL_MS = 1000; // 1 second default interval

    // Build & data helpers
    void buildParameterList();
    void filterParameterList(const QString &filter);
    void loadDataFromFile(const QString &filename);
    void cleanupMemoryMapping();

    // Plotting
    void plotSinglemainwindow();
    void plotPerTabWindow();
    void clearRightArea();

    // Real-time plotting
    void setupRealtimePlotting();
    void startRealtimePlotting();
    void stopRealtimePlotting();
    void updateRealtimeData();
    void clearRealtimeData();
    void updateRealtimeChart();
    void plotRealtimeSingleChart();
    void plotRealtimePerTab();
    void setupRealtimeControls();
    void updateRealtimeWindowLabels();
    void updateRealtimeScrollRange();
    QDateTime getRealtimeWindowStart() const;
    QDateTime getRealtimeWindowEnd() const;
    QPair<QDateTime, QDateTime> getVisibleRealtimeWindow() const;

    // Window helpers
    void updateScrollRangeForWindow(int windowSeconds);
    void getWindowIndicesForApply(int &i0, int &i1,
                                  const QDateTime &t0, const QDateTime &t1) const;

    // Utils
    void downsample(const QVector<QPointF> &src, QVector<QPointF> &dst, int maxPts) const;
    void applyTheme(bool dark);
    QString defaultPicturesDir() const;
    QString defaultDocumentsDir() const;

    // Size adjustment helper
    void adjustLayoutForSize(int width, int height);

    // Time conversion
    int getSecondsFromTimeUnit(int unitIndex, int value) const;
    void updateTimeValueRange(int unitIndex);
    void updateTimeValueRange2(int unitIndex);
    QString formatTimeFromSeconds(int seconds) const;

    // New: Cycle value color scale functions
    void updateColorScale();
    QColor getColorForCycleValue(quint8 cycleValue) const;
    void createModeLegends();
    void updateModeLegends();

    // Helper functions
    void disableControlsForRealtime(bool realtimeEnabled);
    void updateMemoryUsageDisplay();
    void applyMemoryLimit();
    QString formatElapsedTime(qint64 ms) const;
    QString formatMemorySize(qint64 bytes) const;
    int calculateMaxPointsFromMemoryLimit(int memoryLimitMB, int paramCount);
    void restoreParameterSelections();

    // Setup connections after UI is loaded
    void setupConnections();


    // Setup chart widgets (now done in constructor)
    void setupChartWidgets();

protected:
    bool eventFilter(QObject *obj, QEvent *event) override;

};

#endif // MAINWINDOW_H
