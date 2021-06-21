# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:10:42 2021

@author: Nik
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==============================================")
    print(" TRANSAKSI BIAYA EKSPEDISI ")
    print("==============================================")
    print(" a = Surabaya")
    print(" b = Bandung")
    print(" ")
#jika menggunakan list Kode dibawah ini, maka metode yang digunakanadalah mendeteksi indeks value yang terpilih pada list kode. caranya: melakukan pencarian pada list kode menggunakan 
# nilai kode yang diinputkan
    kode =['a','b']

    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]

    pilihan = input(">> Masukkan Kode Tujuan = ")
    #identifikasi Indeks list berdasarkan pilihan
    # baca berulang2 index dalam list kode, jika value sama dengan value pilihan, ambil index nya dengan metode while
    index = 0
    while index < len(kode):
        if kode[index] == pilihan:

            print(">>> Pilihan Tujuan   = " + kota[index ])
            print(">>>          Jarak   = " + str(jarak[index]) + " km")
            print(">>>  Ongkir per Km   = Rp. " + str(ongkirperkm[index]))
#tahap hitung biaya
            ongkir = jarak[index] * ongkirperkm[index]
#tampilkan biaya kirim
            print(">>>> Total           = Rp. " + str(ongkir))
            print(" ")
            print("==============================================")
	#untuk membaca index dari 0 -> index 0 adalah kode a(surabaya), 
	#fungsi index + 1 adalah misal anda memlilih kode b maka akan dibaca index 0+1=1 jadi kode b ada index ke 1, dst
        index = index + 1 
        
#inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break