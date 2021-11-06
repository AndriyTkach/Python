import cmd_parser as p
import pytest
from mock import patch
from argparse import Namespace
import os



@pytest.mark.parametrize("fname, exp_res", [("a.jpg", True),
                                            ("tiff.tiff", True),
                                            ("a.jfg", False),
                                            (0, False)])
def test_is_image(fname, exp_res):
    assert p.is_image(fname) == exp_res


@pytest.mark.parametrize("filename", [("a.jpg"),("a.jfg")])
@patch('cmd_parser.output')
@patch('cmd_parser.is_image')
def test_show_images(mock1, mock2, filename):
    dir = os.path.dirname(os.path.abspath(__file__))
    p.show_images(dir)
    mock1.assert_called()
    if p.is_image(filename):
        mock2.assert_called()
    else:
        mock2.assert_not_called()


@pytest.mark.parametrize("str_size, output", [("1m", 1048576),
                                              ("5K", 1024*5),
                                              ("100b", 100),
                                              ("4q", -1)])
def test_get_bytes(str_size, output):
    assert p.get_bytes(str_size) == output
    

@patch('argparse.ArgumentParser')
def test_argument_parser(mock):
    p.parse_command()
    mock.assert_called()


@pytest.mark.parametrize("cmd",     [("duplicates"),
                                     ("old"),
                                     ("large"),
                                     ("noncommand")])
@patch('cmd_parser.parse_command')
@patch('cmd_parser.check_for_duplicates')
@patch('cmd_parser.show_old_files')
@patch('cmd_parser.show_large')
def test_main(mock1, mock2, mock3, mock4, cmd):
    mock4.return_value = Namespace(command=cmd, size="1m", 
                                   path=os.path.dirname(os.path.abspath(__file__)), \
                                   output=None, help=False)
    p.main()
    mock4.assert_called_once()
    if cmd == "duplicates":
        mock3.assert_called_once()
    elif cmd == "old":
        mock2.assert_called_once()
    elif cmd == "large":
        mock1.assert_called_once()
    else:
        mock3.assert_not_called()
        mock2.assert_not_called()
        mock1.assert_not_called()




@patch('cmd_parser.output')
def test_old_and_duplicates(mock):
    dir = os.path.dirname(os.path.abspath(__file__)) + "\\images"
    p.show_old_files(dir)
    mock.assert_called()
    p.check_for_duplicates(['duplicates', dir])
    mock.assert_called()
    
