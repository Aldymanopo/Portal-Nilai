const dataMahasiswa = {
    namaDepan: "Aldy",
    namaBelakang: "Manoppo",
    nilai: [
        { matkul: "Bahasa Inggris", angka: 85 },
        { matkul: "Pemrograman", angka: 90 },
        { matkul: "Basis Data", angka: 88 }
    ]
};

function tampilkanNilai() {
    // 1. Ambil elemen HTML tempat kita akan menaruh data
    const areaHasil = document.getElementById('area-hasil');
    const namaMhs = document.getElementById('nama-mhs');
    const tabelBody = document.getElementById('tabel-body');

    // 2. Isi Nama Mahasiswa
    namaMhs.innerText = "Nama: " + dataMahasiswa.namaDepan + " " + dataMahasiswa.namaBelakang;

    // 3. Kosongkan tabel dulu (agar tidak dobel jika tombol ditekan 2x)
    tabelBody.innerHTML = "";

    // 4. Masukkan data nilai ke dalam tabel (Looping)
    dataMahasiswa.nilai.forEach(function(item) {
        // Buat baris baru (tr)
        let baris = document.createElement('tr');

        // Isi kolom Mata Kuliah
        let kolMatkul = document.createElement('td');
        kolMatkul.innerText = item.matkul;

        // Isi kolom Nilai
        let kolAngka = document.createElement('td');
        kolAngka.innerText = item.angka;

        // Gabungkan ke dalam baris
        baris.appendChild(kolMatkul);
        baris.appendChild(kolAngka);

        // Masukkan baris ke tabel
        tabelBody.appendChild(baris);
    });

    // 5. Munculkan area hasil (ubah display none jadi block)
    areaHasil.style.display = "block";
}
