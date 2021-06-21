# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:17:19 2021

@author: Nik
"""

#Pemilik Toko bahan bangunan UD. Subur memesan sebuah program kepada Anda untuk dapat menampilkan  beberapa bahan bangunan yang dijualnya pada komputer. Sehingga konsumen dapat memilih dan membeli  barang dalam jumlah yang diinginkannya dan mengetahui jumlah uang yang harus dibayarnya. Berikut daftar  bahan bangunan yang dijualnya: 
#a. Asbes Gelombang @ Rp60.000 
#b. Cat Tembok Dulux 1Galon @ Rp250.000 
#c. Cat Tembok Avian 1 Galon @ Rp350.000 
#d. Aquaproof 5 Kg @ Rp50.000 
#e. Seng 2mm @ Rp70.000 
#f. Spandeks 1mm @ Rp92.000 
#Pembeli akan diberikan potongan 5% bila total pembelian sebelum PPN bernilai minimal Rp 500.000 Dari seluruh total pembayaran tersebut akan dikenakan pajak PPN 2%.

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
#deskripsi :    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("              Transaksi UD.Matahari")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("A = ASBES GELOMBANG")
    print("B = CAT TEMBOK DULUX 1 GALON")
    print("C = CAT TEMBOK AVIAN 1 GALON")
    print("D = AQUAPROOF 5 KG")
    print("E = SENG 2Mm")
    print("E = SPANDEK 1Mm")
    print(" ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Nilai :
    kode =['A','B','C','D','E','F']
    NAMA_BARANG = ['ASBES GELOMBANG','CAT TEMBOK DULUX 1 GALON', 'CAT TEMBOK AVIAN 1 GALON', 'AQUAPROOF 5 KG', 'SENG 2Mm','SPANDEK 1Mm']
    HARGA = [60000,250000,350000,50000,70000,92000]
    Diskon = 0.05
    PPN = 0.02
    Minimaldiskon =  500000
    TotalAwal = 0
    NilaiDiskon = 0
    
#Input 
    pilih = input("KODE PEMBELIAN               = ")    

    #MENENTUKAN PILIHAN
    index = 0
    while index < len(kode):
        if kode[index] == pilih:

            print("JENIS PEMBELIAN                     = " + NAMA_BARANG[index])
            print("HARGA BARANG                        = " + str (HARGA[index]))

            

    #JUMLAH PEMBELIAN AWAL
            JmlBeli = int(input("MASUKAN JUMLAH BARANG YANG DI BELI = "))
            
            if JmlBeli > 0:
                TotalAwal = HARGA[index] * int(JmlBeli)
                print(">> Total Awal                   = Rp " + str (TotalAwal))
            
            PPN = 0.01 * HARGA[index] * JmlBeli
            print("PPN                             =      " + str (PPN))
            
    #POTONGAN HARGA
            if (TotalAwal) > Minimaldiskon:
                NilaiDiskon = int(TotalAwal) * float(Diskon)
                print("Nilai Diskon                    =     " + str (NilaiDiskon))
            else: 0

    #JUMLAH TRANSAKSI
            TotalBayar = int(TotalAwal) - int(NilaiDiskon) + PPN
            print("Total dibayarkan                = Rp " + str (TotalBayar))
            print()
            print("=======================================================")
            
        index = index + 1

    #inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break