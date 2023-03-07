import 'package:flutter/material.dart';

void main() {
  runApp(myApp());
}

class myApp extends StatelessWidget {
  @override
  Widget build(BuildContext ctx) {
    return MaterialApp(
      theme: ThemeData(
          appBarTheme: AppBarTheme(backgroundColor: Colors.amber),
          scaffoldBackgroundColor: Colors.grey),
      debugShowCheckedModeBanner: false,
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  /// common mistake
  final items = List<String>.generate(29, (index) => 'item ${index + 1}');

  final controller = TextEditingController();
  @override
  Widget build(BuildContext ctx) {
    return Scaffold(
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      floatingActionButton: FloatingActionButton(
        mini: true,
        onPressed: () {
          showModalBottomSheet(
              context: context,
              builder: (ctx) {
                return SizedBox(
                  height: 110,
                  child: Column(
                    children: [
                      TextField(
                        controller: controller,
                        decoration: InputDecoration(
                          hintText: 'New TODO',
                          border: OutlineInputBorder(),
                        ),
                      ),
                      ElevatedButton(
                          onPressed: () {
                            setState(() {
                              if (controller.text.isNotEmpty) {
                                items.add(controller.text);
                                controller.text = '';
                              }
                            });
                            Navigator.of(context).pop();
                          },
                          child: Text('Add'))
                    ],
                  ),
                );
              });
        },
        child: Icon(Icons.add),
      ),
      appBar: AppBar(
        actions: [
          IconButton(
              onPressed: () {
                setState(() {
                  items.clear();
                });
              },
              icon: Icon(Icons.delete))
        ],
        centerTitle: true,
        title: const Text(
          'TODO',
          style: TextStyle(),
        ),
      ),
      drawer: const Drawer(),
      body: items.length == 0
          ? Center(
              child: Text('you have no Todos ya batal'),
            )
          : Center(
              child: SizedBox(child: ListView.builder(
                // itemCount: items.length,
                itemBuilder: (context, index) {
                  return Column(
                    children: [
                      ...items.map((item) {
                        return Container(
                          margin: EdgeInsets.all(10),
                          height: 50,
                          decoration: BoxDecoration(color: Colors.blue),
                          child: Card(
                            margin: EdgeInsets.all(10),
                            elevation: 20,
                            shadowColor: Colors.amber,
                            child: Center(child: Text(item)),
                          ),
                        );
                      }).toList(),
                    ],
                  );
                },
              )),
            ),
    );
  }
}
