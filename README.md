# omni_robot
Code ini merupakan package yang digunakan pada sistem
diamana terdiri dari Omni_cam untuk akses kamera
Omni_bot untuk pergerakan robot

Omni_bot terdiri dari 1 program launch & 4 Program Node.
Omni_bot.launch = berisi program untuk menjalankan file driver_node , encoder dan sensor secara bersamaan.

file driver_node berisi :
  program untuk stop motor
  program untuk memutar motor

*file encoder.py :
  nama node : encode
  program untuk pembacaan encoder sensor dari ketiga motor
  Output program : pembacaan jumlah pulsa setiap motor
  topic : /counter
  message :
    enc1 int64
    enc2 int64
    enc3 int64
*file encoder.py :
  nama node : encode
  program untuk pembacaan encoder sensor dari ketiga motor
  Output program : pembacaan jumlah pulsa setiap motor
  topic : /counter
  message :
    enc1 int64
    enc2 int64
    enc3 int64
