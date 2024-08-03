"""Users"""
class U:
	def __init__(self, id:str | None=None, birth:str | None=None, username:str | None=None, password:str | None=None, playlists:list[int] | None=None, tracks:list[int] | None=None, friends:list[int] | None=None, recent_plays:list[int] | None=None, active_room:int | None=None, current_play:int | None=None, last_login:str | None=None, ):
		self.D_id = id
		self.D_birth = birth
		self.D_username = username
		self.D_password = password
		self.D_playlists = playlists
		self.D_tracks = tracks
		self.D_friends = friends
		self.D_recent_plays = recent_plays
		self.D_active_room = active_room
		self.D_current_play = current_play
		self.D_last_login = last_login
		
	def gd(self, get_none=False):
		"""Generate dict from schema"""
		output_dict = {}
		for attr, value in vars(self).items():
			if attr.startswith("D_") and (get_none or value is not None):
				keyForOutputDict = attr.split("_")[1]
				output_dict[keyForOutputDict] = value
		return output_dict
	def gk(self, id=False, birth=False, username=False, password=False, playlists=False, tracks=False, friends=False, recent_plays=False, active_room=False, current_play=False, last_login=False, ):
		"""Generate keys' string based on bool params"""
		return f"{'id' if id else ''}{', birth' if birth else ''}{', username' if username else ''}{', password' if password else ''}{', playlists' if playlists else ''}{', tracks' if tracks else ''}{', friends' if friends else ''}{', recent_plays' if recent_plays else ''}{', active_room' if active_room else ''}{', current_play' if current_play else ''}{', last_login' if last_login else ''}"

