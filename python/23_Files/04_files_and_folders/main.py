import os

def katalog(file_path, summ_kb_bit_catalog_file):
    for element in os.listdir(file_path):
        path_el = os.path.join(file_path, element)
        if os.path.isfile(path_el):
            summ_kb_bit_catalog_file[2] += 1
            summ_kb_bit_catalog_file[0] += os.path.getsize(path_el)/1024
        elif os.path.isdir(path_el):
            summ_kb_bit_catalog_file[1] += 1
            katalog(path_el, summ_kb_bit_catalog_file)


file_path = os.path.abspath('..')
summ_kb_bit_catalog_file=[0,0,0]
katalog(file_path,summ_kb_bit_catalog_file)
print(f'Размер каталога (в Кб): {summ_kb_bit_catalog_file[0]}'
      f'\nКоличество подкаталогов: {summ_kb_bit_catalog_file[1]}'
      f'\nКоличество файлов: {summ_kb_bit_catalog_file[2]}')
