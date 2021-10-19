def kasir(nama, member, harga_satuan, jumlah_beli):
	sub_total = harga_satuan * jumlah_beli
	diskon = 0
	if member == 'member':
		member = 'Member'
		if sub_total >= 500000:
			diskon = 20
		elif 200000 <= sub_total <= 400000:
			diskon = 15
		elif 100000 <= sub_total <= 200000:
			diskon = 10
	else:
		member = 'Bukan Member'
		if sub_total >= 500000:
			diskon = 15
		elif 200000 <= sub_total <= 400000:
			diskon = 10
		elif 100000 <= sub_total <= 200000:
			diskon = 5

	total = sub_total - sub_total*diskon/100

	print(nama, '''total pembelian anda adalah Rp ''', total, '''dengan rincian :
	================================================================
	Jenis Pelanggan : ''', member,'''
	Harga Satuan 	: ''', harga_satuan,'''
	Jumlah Beli 	: ''', jumlah_beli,'''
	Sub Total 	: ''', sub_total,'''
	Diskon 		: ''', diskon, '''%
	Potongan 	: ''', sub_total*diskon/100)


	# print(nama, 'total pembelian anda adalah Rp ', total, 'dengan rincian :')
	# print('================================================================')
	# print('Jenis Pelanggan : ', member)
	# print('Harga Satuan : ', harga_satuan)
	# print('Jumlah Beli : ', jumlah_beli)
	# print('Sub Total : ', sub_total)
	# print('Diskon : ', diskon, '%')
	# print('Potongan : ', sub_total*diskon/100)


if __name__ == '__main__':
	nama 			= input('Nama : ')
	member 			= input('Jenis Pelanggan (Member/Bukan) : ').lower()
	harga_satuan 	= float(input('Harga Satuan Barang : '))
	jumlah_beli 	= int(input('Jumlah Barang : '))

	kasir(nama, member, harga_satuan, jumlah_beli)