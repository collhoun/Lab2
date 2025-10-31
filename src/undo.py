from src.rm import do_rm
from src.move import do_move
from logging import getLogger

logger = getLogger(__name__)


def do_undo(command: str, list_of_tokens: list):
    """function mays user to cancel cp rm mv commnands

    Args:
        command (str): command user wants to cancel
        list_of_tokens (list): tokens of previous comand

    Raises:
        ValueError: erorr if there is no such comand
    """

    if command == 'cp':
        if len(list_of_tokens) == 4:
            option, file_for_recopy, target_dir, dir_before_action = list_of_tokens
            if '\\' in file_for_recopy:
                dir_name = file_for_recopy.split('\\')[-1]
            else:
                dir_name = file_for_recopy
            logger.info('undo cp')
            do_rm(f'{target_dir}\\{dir_name}', '-r')

        else:
            file_for_copy, target_dir, dir_before_action = list_of_tokens
            if '\\' in file_for_copy:
                dir_name = file_for_copy.split('\\')[-1]
            else:
                dir_name = file_for_copy
            logger.info('undo cp')
            do_rm(f'{target_dir}\\{dir_name}')

    elif command == 'mv':
        file_to_move_back, target_dir_to_move_from, dir_before_action = list_of_tokens
        logger.info('undo mv')
        do_move(f'{target_dir_to_move_from}\\{file_to_move_back.split('\\')[-1]}',
                f'{dir_before_action}\\{'\\'.join(file_to_move_back.split('\\')[:-1])}')

    elif command == 'rm':
        if len(list_of_tokens) == 3:
            option, file_to_restore, dir_before_action = list_of_tokens
            filename_to_remove = file_to_restore.split(
                '\\')[-1] if '\\' in file_to_restore else file_to_restore
            logger.info('undo rm')
            do_move(f'src\\.trash\\{filename_to_remove}',
                    f'{dir_before_action}\\{'\\'.join(file_to_restore.split('\\')[:-1])}')
        else:
            file_to_restore, dir_before_action = list_of_tokens
            filename_to_remove = file_to_restore.split(
                '\\')[-1] if '\\' in file_to_restore else file_to_restore
            logger.info('undo rm')
            do_move(f'src\\.trash\\{filename_to_remove}',
                    f'{dir_before_action}\\{'\\'.join(file_to_restore.split('\\')[:-1])}')

    else:
        logger.error('Невозможно отменить действие команды %s', command)
        raise ValueError(f"Невозможно отменить действие команды {command}")


if __name__ == '__main__':
    pass
