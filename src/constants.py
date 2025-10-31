from src.cat import do_cat
from src.cd import do_cd
from src.cp import do_cp
from src.ls import do_ls
from src.move import do_move
from src.rm import do_rm
from src.zipper import do_zip, do_tar, do_unzip, do_untar
from src.grep import do_grep
from src.history import do_history
from src.undo import do_undo

COMMANDS_DICTIONARY: dict = {
    'cat': do_cat,
    'cd': do_cd,
    'cp': do_cp,
    'ls': do_ls,
    'mv': do_move,
    'rm': do_rm,
    'zip': do_zip,
    'unzip': do_unzip,
    'tar': do_tar,
    'untar': do_untar,
    'grep': do_grep,
    'history': do_history,
    'undo': do_undo
}
