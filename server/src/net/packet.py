# misc
MSG_NOP = 0x11

# from client.py
MSG_INIT = 0x00

# when the client detects a "hack attempt"
# the client checksums all of its imortant variables and also does range checks
MSG_CLIENT_ERROR = 0x10

MSG_PLAYER_DEATH = 0x03
MSG_OTHER_PLAYER_NOT_FOUND = 0x04
MSG_PVP_HIT_PLAYER = 0x05
MSG_CHAT = 0x06
MSG_HIT_MOB = 0x08
MSG_HAT_CHANGE = 0x0a
MSG_GET_NUM_PLAYERS = 0x0c
MSG_SPAWN_MOB = 0x0f
MSG_LEVEL_UP = 0x14

MSG_UDP_PLAYER_POS_CHANGE = 0x01
MSG_UDP_PLAYER_SPRITE_CHANGE = 0x02
MSG_UDP_PING = 0x0b

RESP_NEW_PLAYER = 0x00
RESP_PLAYER_DEATH = 0x03
RESP_DMG_PLAYER = 0x05
RESP_CHAT = 0x06
RESP_HIT_MOB = 0x08
RESP_HAT_CHANGE = 0x0a
RESP_PING = 0x0b
RESP_NUM_PLAYERS = 0x0c
RESP_LEVEL_UP = 0x14

# from world.py
RESP_MOB_DEATH = 0x09

# from mob.py
RESP_MOB_STATUS = 0x07

# from account_server.py
MSG_REGISTER = 0x00
MSG_LOGIN = 0x01
MSG_SAVE = 0x03

RESP_LOGIN_ACCEPT = 0x01
RESP_DENY_REQUEST = 0x02
RESP_SUCCESS = 0x03

# from game_server.py
RESP_CLIENT_DISCONNECT = 0x03
RESP_CHAT = 0x06
