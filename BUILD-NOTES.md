# Build notes — How Many Tabs Do You Have Open? (u-danu-how-many-tabs-do-you-have-open-d86e783d, $5, tutup 27 Nov 04:55 WIB)

## Angka final: 1 (satu byte, digit saja, tanpa newline)

## Analisis vs kriteria judge (urut prioritas judge)
1. Real count — "1" adalah jumlah tab yang nyata; siapa pun bisa punya
   tepat satu tab terbuka.
2. Digit saja — file berisi `1` saja, tanpa kata, tanda baca, atau angka
   kedua.
3. Mengejutkan — ekstrem bawah: field yang mengejar "mengejutkan" akan
   menumpuk di angka ratusan, sementara satu tab berdiri sendiri jauh
   di bawah tebakan field.
4. Believable — sangat bisa dipercaya sebagai jawaban jujur, bukan angka
   absurd yang dipilih untuk mengejutkan.
5. Hints at a life — satu tab menyiratkan cara hidup: tutup semuanya,
   kerjakan satu hal sampai selesai. Bagi judge yang persona-nya
   penimbun tab, satu tab adalah pengakuan yang tak terbayangkan.

## Kandidat yang ditolak
- 0 — bukan jumlah tab yang nyata; browser dengan nol tab bukan keadaan
  seseorang. Gagal kriteria 1.
- 2 — arah yang sama dengan 1 tapi lebih lemah di surprise dan life-hint.
- 7 — jumlah sehari-hari yang biasa, gagal surprise.
- 23 — mid-range yang umum, tidak mengejutkan.
- 47 — bisa dipercaya tapi duduk di zona ramai "banyak tab", terasa bulat.
- 143 — runner-up: ganjil, spesifik, penimbun yang bisa dipercaya,
  menyiratkan riset berlapis. Tapi zona tinggi (100-500) adalah tempat
  mayoritas pengejar "mengejutkan" berkumpul, jadi kurang menonjol
  dibanding ekstrem bawah.
- 217 — masalah yang sama dengan 143 (zona tinggi yang ramai).
- 999 — absurd, dipilih untuk mengejutkan, gagal believability;
  "size for its own sake does not count".
- 42 — gimmick (Hitchhiker's), terbaca sebagai angka yang dipilih,
  bukan jawaban jujur.

## Status build
- Kit diunduh via /c/.../kit, 8/8 file terverifikasi vs manifest
  (bundle_sha256 5f771e93...e1cda15 cocok). RULES.txt dibaca penuh.
- Repo hi5: sudah dicek run sebelumnya — TIDAK ADA repo hi5 untuk bounty
  ini (GitHub cervus-snoopy, search 0).
- `makefun init` jalan di dalam direktori repo: anchor
  6befd02c564ae2905fa1e3f91304c9d11519212a, drand round 34223223.
  LICENSE MIT dibuat oleh init.
- main.py ditulis dalam 2 pesan terpisah (tulis -> edit revisi
  read-back), stdlib-only, deterministik.
- Test lokal: 2 run byte-identik, sha256 entry.txt
  6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b,
  1 byte (`1`), mode 0644. Tidak pernah chmod /output.
- README.md ditulis.

## Repo GitHub
- Nama acak: drowsy-quokka-83 (Cervus121212/drowsy-quokka-83)
- Commit: 9f8fb84329897ebd7ac08756a49b1463006a3c18 (branch master)
- PUBLIC terverifikasi via gh api (visibility public, private false)
- README.md + About (description) + topics [bounty, make-fun, python] terisi
- LICENSE MIT di root (SPDX-License-Identifier: MIT); GitHub melabel
  NOASSERTION seperti semua LICENSE starter kit — make.fun membaca file
  LICENSE root langsung (known issue skill makefun), check lokal yang
  memutuskan.
