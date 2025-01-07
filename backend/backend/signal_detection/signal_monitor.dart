import 'dart:async';

class SignalMonitor {
  final List<String> rogueSignals = [
    "FakeCellTower1",
    "SuspiciousWiFiNetwork"
  ];

  Stream<String> monitorSignals() async* {
    while (true) {
      await Future.delayed(const Duration(seconds: 5));
      yield "Detected: FakeCellTower1";
    }
  }
}
