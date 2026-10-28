#include <iostream>
#include <queue>
using namespace std;

struct Pasien {
    int nomor;
};

int main() {
    queue<Pasien> antrian;
    int pilihan, counter = 0;

    do {
        cout << "\n=== MENU KLINIK ===\n";
        cout << "1. Ambil nomor antrian\n";
        cout << "2. Panggil pasien berikutnya\n";
        cout << "3. Lihat antrian saat ini\n";
        cout << "4. Keluar\n";
        cout << "Pilih : ";
        cin >> pilihan;

        switch(pilihan) {
            case 1:
                counter++;
                antrian.push({counter});
                cout << "Pasien mendapat nomor antrian: " << counter << endl;
                break;
            case 2:
                if (!antrian.empty()) {
                    cout << "Memanggil pasien nomor " << antrian.front().nomor << endl;
                    antrian.pop();
                } else {
                    cout << "Tidak ada pasien dalam antrian.\n";
                }
                break;
            case 3:
                if (!antrian.empty()) {
                    cout << "Nomor antrian saat ini: ";
                    queue<Pasien> temp = antrian;
                    while (!temp.empty()) {
                        cout << temp.front().nomor << " ";
                        temp.pop();
                    }
                    cout << endl;
                } else {
                    cout << "Antrian kosong.\n";
                }
                break;
        }
    } while (pilihan != 4);

    return 0;
}

