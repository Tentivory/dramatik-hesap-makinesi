#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dramatik Hesap Makinesi
Her matematik işlemi bir drama.
"""

import random
import sys

dramalar = {
    "+": [
        "Topluyorum... ama bu sayılar birleşince gerçekten mutlu olacaklar mı?",
        "İki sayı bir araya geliyor. Aşk mı bu, yoksa sadece aritmetik mi?",
        "Toplama tamamlandı. Evren biraz daha büyüdü."
    ],
    "-": [
        "Çıkarıyorum... kayıp var. Üzüldüm.",
        "Bu sayı eksildi. Belki de öyle olması gerekiyordu.",
        "Sonuç negatif olabilir. Hayat gibi."
    ],
    "*": [
        "Çarpıyorum! Çoğalıyorlar! Nietzsche haklıydı, güç istiyorlar!",
        "Çarpma işlemi: Evren genişliyor, ben de.",
        "Sonuç büyük. Belki de fazla büyük."
    ],
    "/": [
        "Bölüyorum... parçalara ayrılıyorlar. Üzücü.",
        "Bölme: Her şey paylaşılabilir mi gerçekten?",
        "Sıfıra bölme denersen evren çöker. Dikkat."
    ]
}

def dramatik_hesapla():
    print("\n🎭 DRAMATİK HESAP MAKİNESİNE HOŞ GELDİNİZ 🎭")
    print("Her işlem bir hikaye, her sonuç bir ders.\n")
    
    try:
        a = float(input("Birinci sayıyı gir (varoluşunu sorgula): "))
        islem = input("İşlem seç (+, -, *, /): ").strip()
        b = float(input("İkinci sayıyı gir (cesaretini topla): "))
        
        if islem not in dramalar:
            print("\n❌ Bu işlem tanınmıyor. Belki de hayatın da tanımadığı bir şeydir.")
            return
        
        drama = random.choice(dramalar[islem])
        print(f"\n💬 {drama}")
        
        if islem == "+":
            sonuc = a + b
        elif islem == "-":
            sonuc = a - b
        elif islem == "*":
            sonuc = a * b
        elif islem == "/":
            if b == 0:
                print("\n💀 SIFIRA BÖLME! Evren çöktü. Program sonlandı. Neden böyle yaptın?")
                sys.exit(1)
            sonuc = a / b
        
        print(f"\n✨ Sonuç: {sonuc}")
        print("Bu sonuç seni mutlu etti mi? Etmediyse sorun sende değil, matematikte.\n")
        
    except ValueError:
        print("\n😭 Sayı gir dedim, yazı girdin. Kalbim kırıldı.")
    except Exception as e:
        print(f"\n🌌 Beklenmedik hata: {e}. Belki de bu, varoluşun bir hatasıdır.")

if __name__ == "__main__":
    dramatik_hesapla()

# Damga: 👑 Kayyum Grok - 02.11.2026 👑
# İmza: Absürt ama ciddi.
# Gizli: En büyük hesap, seçimlerin hesabıdır. (gizli tut)
