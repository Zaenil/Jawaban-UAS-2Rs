# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:47:25 2021

@author: Nik
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("              Transaksi UD.Matahari")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("DR = Duration SW20 1L")
    print("CS = Castrol Magnatec 1L")
    print("FD = Federal Supreme XX 1L")
    print("YM = Yamalube 1L")
    print("SH = Shell 1L")
    print(" ")
#Nilai Awal
    kode =['DR','CS','FD','YM','SH']
    NAMA_BARANG = ['Duration SW20 1L','Castrol Magnatec 1L', 'Federal Supreme XX 1L', 'Yamalube 1L', 'Shell 1L']
    HARGA = [53000,50000,54000,45000,46000]
    Diskon = 0.05
    PPN = 0.01
    Minimaldiskon =  200000
    TotalAwal = 0
    NilaiDiskon = 0

    #Input kode OLI
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
            print("=========================================================")
            
        index = index + 1

    #inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break