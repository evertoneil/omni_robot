# omni_robot
Code ini merupakan package yang digunakan pada sistem
dimana terdiri dari :
1. Omni_cam untuk akses kamera
2. Omni_bot untuk pergerakan robot

Omni_bot terdiri dari 1 program launch & 4 Program Node.
Omni_bot.launch = berisi program untuk menjalankan file driver_node2 , encoder dan sensor secara bersamaan.

file *driver_node2* berisi :
  1.program untuk stop motor
  2.program untuk memutar motor
  3.program untuk mengkalkulasi RPM Motor
  4.Program PID (optional)
  4.program 'master' untuk menerima semua value

file *encoder.py* berisi :
  program untuk pembacaan encoder sensor dari ketiga motor
  Output program : pembacaan jumlah pulsa setiap motor
    
file *odo.py* berisi :
  program untuk menerima input posisi tujuan , kalkulasi kecepatan tiap motor dan jumlah putaran yang diperlukan
  tiap-tiap motor untuk reach end position tersebut.
  Output program : (2 topic) PWM motor , RPM dibutuhkan motor, putaran motor yg dibutuhkan

file *sensor.py* berisi :
  program untuk menerima input sensor dan kalkulasi dalam cm.
