# omni_robot
Code ini merupakan package yang digunakan pada sistem
diamana terdiri dari Omni_cam untuk akses kamera
Omni_bot untuk pergerakan robot

Omni_bot terdiri dari 1 program launch & 4 Program Node.
Omni_bot.launch = berisi program untuk menjalankan file driver_node , encoder dan sensor secara bersamaan.

file driver_node berisi :
  program untuk stop motor
  program untuk memutar motor

file encoder.py :
  nama node : encode
  program untuk pembacaan encoder sensor dari ketiga motor
  Output program : pembacaan jumlah pulsa setiap motor
  topic : /counter
  message :
    enc1 int64
    enc2 int64
    enc3 int64
file odometry.py :
  nama node : odometry
  program untuk menerima input posisi tujuan , kalkulasi kecepatan tiap motor dan jumlah putaran yang diperlukan
  tiap-tiap motor untuk reach posisi tersebut.
  Output program : (2 topic) kecepatan motor , putaran motor yg dibutuhkan
  topic 1 : /kecepatan  (dalam perbandingan yang dikoneversi menjadi 0 - 255)
    message :
    v1 float64 
    v2 float64
    v3 float64
  topic 2 : /putaran (dalam satuan derajat {degree} )
    message :
    deg1 int 
    deg2 int
    deg3 int
