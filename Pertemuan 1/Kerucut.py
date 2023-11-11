#Program menghitung luas dan volume kerucut

# Pertemuan 1
# Programmer: Mohammad rizy imansyah
# Tanggal:  11 November 2023

jariJari = 5;
sisiKerucut = 10;
tinggi = 15;

luasSelimutKerucut = 3.14*jariJari+tinggi;
luasPermukaanKerucut = 3.14*jariJari*sisiKerucut + 3.14*jariJari**2;
volumetKerucut = 3.14*jariJari**2 * tinggi/3;

print('luas selimut kerucut', luasSelimutKerucut)
print('luas permukaan kerucut', luasPermukaanKerucut)
print('luas volume kerucut', volumetKerucut)