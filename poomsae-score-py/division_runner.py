import time
import sql_tools.division_tools as dtools
import sqlite3 as sql
import threading

class DivisionRunner:
	def __init__(self, db_path):
		# Timer variables
		self.start_time = None
		self.end_time = None
		self.timed_out = False
		self.timer_thread_flag = False

		# Sql variables
		self.connection = sql.connect(db_path)
		self.round_num = None
		self._load_file()


		# Runner variables
		self.active_controllers = []


		self.reset_timer()

	def _load_file(self):
		self.p_time = dtools.get_round_comp_time(self.connection)

	def start_timer(self):
		self.start_time = time.time()
		self.timer_thread_flag = True
		self.timer_thread = threading.Thread(target=self._timer_thread)
		self.timer_thread.start()

	def _timer_thread(self):
		while self.timer_thread_flag:
			self.end_time = time.time()
			if self.p_time - (self.end_time - self.start_time) <= 0:
				self.start_time = self.start_time + self.p_time
				self.timed_out = True
				break
			time.sleep(0.1)

	def stop_timer(self):
		if self.timer_thread:
			self.timer_thread_flag = False
			self.timer_thread.join()
			self.timer_thread = None

	def reset_timer(self):
		t = time.time()
		self.start_time = float(t)
		self.end_time = float(t)
		self.timed_out = False

	def get_current_time(self):
		t = self.p_time - (self.end_time - self.start_time)
		m = int(t//60)
		s = t%60

		if m > 0:
			return '{:d}:{:.1f}'.format(m, s)
		return '{:.1f}'.format(s)

	def start_score_threads(self):
		pass

	def _wait_scores(self):
		pass

	def get_next_round(self):
		return dtools.get_next_round(self.connection)

	def _wait_scores(self):
		pass

	def __del__(self):
		self.stop_timer()
		self.connection.close()
