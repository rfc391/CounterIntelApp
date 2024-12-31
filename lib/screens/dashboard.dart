import 'package:flutter/material.dart';
import '../backend/signal_detection/signal_monitor.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final SignalMonitor _signalMonitor = SignalMonitor();
  String _lastSignal = "No threats detected.";

  @override
  void initState() {
    super.initState();
    _signalMonitor.monitorSignals().listen((signal) {
      setState(() {
        _lastSignal = signal;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Dashboard")),
      body: Center(
        child: Text(
          _lastSignal,
          style: const TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
