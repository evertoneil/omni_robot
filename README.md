# omni_robot
Code ini merupakan package yang digunakan pada sistem
dimana terdiri dari :
1. Omni_cam untuk akses kamera
2. Omni_bot untuk pergerakan robot

Omni_bot terdiri dari 1 program launch & 4 Program Node.
Omni_bot.launch = berisi program untuk menjalankan file driver_node2 , encoder & sensor secara bersamaan.

file *driver_node2* berisi :
1.program untuk run & Stop motor
2.program untuk mengkalkulasi RPM Motor
3.Program PID (optional)
4.program 'master' untuk menerima semua value dari program lain

file *encoder.py* berisi :
  program untuk pembacaan encoder sensor dari ketiga motor
  Output program : pembacaan jumlah pulsa setiap motor dalam satuan pulsa/'tick'
    
file *odo.py* berisi :
  program untuk input posisi tujuan user, mengkalkulasi kecepatan tiap motor(inverse kinematics) dan jumlah pulsa(odometri) yang diperlukan
  tiap-tiap motor untuk reach end position tersebut.
  Output program : (2 topic) PWM motor , RPM dibutuhkan motor, pulsa motor yg dibutuhkan

file *sensor.py* berisi :
  program untuk menerima input sensor dan kalkulasi dalam cm kemudian di publish

file *tabrak.py* berisi :
  program untuk mendeteksi apakah ada limit switch yang ditekan, bila iya maka program akan berhenti.
  
Alur cara kerja ROBOT:

1. Nyalakan Switch (Hardware) robot
2. Cek IP masing-masing dari Jetson & Raspberry pi
3. Ganti ROS_master_IP di masing-masing /.bashrc kedua kontroller dengan ip address Raspberry Pi.
4. Execute di terminal roslaunch omni_bot omni_bot.launch (raspi)
5. Execute di terminal baru rosrun omni_bot sensor.py (raspi)
6. Execute di terminal baru rosrun omni_cam camera.py (jetson nano)
7. execute di terminal baru rosrun omni_bot odo.py (raspi) untuk memasukkan input posisi
8. Robot akan bergerak ke posisi tujuan, berputar untuk mendeteksi adanya objek,lalu berhenti dan mengkalkulasi jarak & ukuran
9. Apabila ingin pindah ke posisi lain, cancel semua proses dan ulangi dari step 4
