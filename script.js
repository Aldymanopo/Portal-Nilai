function ambilDataNilai() {
    const btn = document.getElementById("btn-muat");
    const loading = document.getElementById("loading");
    const tabel = document.getElementById("tabel-nilai");
    const tbody = document.getElementById("isi-tabel");

    // Tampilkan loading
    btn.disabled = true;
    loading.style.display = "block";
    tabel.style.display = "none";

    // Panggil API Python
    fetch('/api/get-nilai')
        .then(response => response.json())
        .then(data => {
            // Kosongkan tabel lama
            tbody.innerHTML = "";

            // Masukkan data baru (Looping)
            data.forEach(item => {
                let row = `<tr>
                    <td>${item.nama}</td>
                    <td>${item.matkul}</td>
                    <td><strong>${item.nilai}</strong></td>
                </tr>`;
                tbody.innerHTML += row;
            });

            // Tampilkan tabel, sembunyikan loading
            loading.style.display = "none";
            tabel.style.display = "table";
            btn.disabled = false;
            btn.innerText = "Refresh Nilai";
        })
        .catch(error => {
            console.error('Error:', error);
            loading.innerText = "Gagal mengambil data.";
        });
}