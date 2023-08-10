
import create_fundament
import write_data
import time
if __name__ == '__main__':
	print("Ожидание разворачивания базы")
	time.sleep(60)
	start_time = time.time()
	create_fundament.create_env_baza()
	write_data.write_data()
	print("---------------------------- %s seconds ----------------------------" % (time.time() - start_time))
	print("Работа с данными завершена")