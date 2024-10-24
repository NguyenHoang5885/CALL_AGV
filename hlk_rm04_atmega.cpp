//code atmega gửi html đến flask
#include <Arduino.h>
#include <ArduinoJson.h>
#include "SoftwareSerial.h"

DynamicJsonDocument doc(1024);
SoftwareSerial flask(19, 18); // RX, TX ATMEGA2560 connect to GPI03: RX, GPIO5: TX HLK-RM04

void sendHttpPost() {
  // Chuẩn bị nội dung của yêu cầu HTTP POST
  String postData;
  serializeJson(doc, postData);

  String request = String("POST /items HTTP/1.1\r\n") +
                   String("Host: 192.168.3.254:5000\r\n") +
                   String("Content-Type: application/json\r\n") +
                   "Content-Length: " + String(postData.length()) + "\r\n" +
                   "\r\n" + postData;

  // Gửi yêu cầu đến Flask
  flask.print(request); // Hoặc dùng Serial.print nếu bạn muốn kiểm tra đầu ra
}

void Json() {
  doc["Bo_goi_AGV"] = "Bo_goi_AGV";

  // Gọi hàm để gửi yêu cầu HTTP POST
  sendHttpPost();
}

void setup() {
  Serial.begin(115200);
  flask.begin(115200);
}

void loop() {
  Json();
  Serial.println();
  delay(500);
}