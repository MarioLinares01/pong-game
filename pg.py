#! /usr/bin/env python3
# Mario Linares


"""The entry point for a Pong game."""

from ponggame.game import Pong


def main():
    """The main function will run the Pong game."""
    pong = Pong()
    pong.build_scene_graph()
    return pong.run()


if __name__  == '__main__':
    main()