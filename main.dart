import 'package:flutter/material.dart';
import 'screens/dashboard.dart';

void main() {
  runApp(const CounterIntelApp());
}

class CounterIntelApp extends StatelessWidget {
  const CounterIntelApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CounterIntelApp',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const CalculatorScreen(),
    );
  }
}

class CalculatorScreen extends StatelessWidget {
  const CalculatorScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Calculator')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const DashboardScreen()),
            );
          },
          child: const Text('Open CounterIntelApp'),
        ),
      ),
    );
  }
}
