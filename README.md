Work in Progress Demo
=====================

Overview
--------
This is the source code for the demo release of Work in Progress. It is released in the hope people can learn from it and modify it to their needs and wishes.

Requirements
------------
- A relatively modern PC (anything made in the latter half of the 00's will do fine), running either:
    * Windows XP+ (but please do upgrade to a more modern Windows)
    * OS X 10.7+
    * Linux with [glibc](https://www.gnu.org/software/libc/libc.html) or [glibc-compatible libc](http://www.eglibc.org/home) and [X11](http://x.org)
- [Ren'Py 6.17.6](http://renpy.org/dl/6.17.6/) with the [included patches](#patching-renpy)
- Creativity

Patching Ren'Py
---------------
Work in Progress uses a slightly patched Ren'Py to weed out two engine bugs that weren't fixable in time in mainline Ren'Py.
To apply them on a system with a sh-compatible command line and [patch](https://savannah.gnu.org/projects/patch/) or [compatible equivalent](https://svnweb.freebsd.org/base/stable/10/usr.bin/patch/):

```bash
cd /path/to/renpy-6.17.6-sdk
patch -p1 < /path/to/wip/patches/*.patch
```

Alternatively, you can get a pre-patched Ren'Py from [here](https://salty-salty-studios.com/priv/renpy-6.17.6-sdk-patched.zip).

Working with the script
-----------------------
Work in Progress uses a semi-custom script system called `RABBL`. This allows the developers to efficiently manage choice structures and translations.

The game story is handled by the master script file in `game/script/script.rpy`. This file contains the entry point for RABBL and guides the general script flow.
It tells the engine what scenes to perform, what choices should be made and how the results should be handled, centrally.

RABBL introduces the `perform` statement to perform a scene. Essentially, ignoring all the tiny extras RABBL gives us, this calls the label `scene_<name>_<currentlanguage>`.
Likewise, there is also the `choice` statement to perform a choice. This, again, gives us some tiny extras, but also fixes the choice so it can't be made again when rolling back.
It calls `choice_<name>_<currentlanguage>` to display the choice, and relies that said label returns a numeric value indicating what choice was made.

RABBL and, as a result, WiP do not support Ren'Py's built-in translation system because they predate it.
However, RABBL is internationalization-friendly: to translate, all you need to do is copy `game/scripts/en` to your target language (e.g. `game/scripts/fr`), rename all labels from `_en` to `_fr`,
and add the new language to `available_languages` in `game/script/init.rpy`. You then can start translating! Translation requires at least a tiny amount of familiarity with Ren'Py's script format.

All new scenes must be added to the `scenes` variable in `game/script/<language>/init.rpy` in order to be registered with the scene replay system and have their title shown in the pause menu.
They also need an entry in `game/script/sceneshots` if they aren't set to hidden in the scene replay system.

All new characters must be registered using the `characters` and `character_tags` variables in `game/script/<language>/init.rpy`. You don't have to define characters manually: just adding them here will initialize them.

All UI strings are registered in `game/script/<language>/init.rpy` for translation.

For language-specific images, please use the folder `game/vfx/<language>`. Create it if it doesn't exist.

Working with assets
-------------------
Assets are automatically defined from the folders: see `game/resources.rpy` for the exact rules. Currently, they are as follows:

* All images from `game/sprites` get defined as their base/folder name: `game/sprites/caprice/smile.png` becomes `caprice smile` and `game/sprites/allison/smile_eyesclosed.png` becomes `allison smile eyesclosed`.
  They also get adjusted vertically according to the `sprite_offsets` variable, defined in `game/script/init.rpy`.
* All images from `game/bgs` get defined with a `bg` prefix: `game/bgs/apartment/bathroom.png` becomes `bg apartment bathroom`.
* All images from `game/cgs` get defined with a `cg` prefix: `game/cgs/mekki_intro.png` becomes `cg mekki intro`.
* All images from `game/vfx` get defined with a `misc` prefix: `game/vfx/phone.png` becomes `misc phone`.

All music tracks must be added to the `tracks` variable in `game/script/<language>/init.rpy` in order to be registered in the jukebox and have their title shown in the pause menu.

Working with the code
---------------------
Work in Progress's code is managed using the [git](http://git-scm.com/) source code control system. A primer on git is available [here](http://git-scm.com/documentation).

All hacks and additions to Ren'Py are stored in the `game/lib` folder. Try to make game functionality as non-specific to Work in Progress as possible, and store it there. Then the game code can make use of it.

Building installers
--------------------
The `installers` directory contains the source code to the installer scripts used for Work in Progress. There are two subdirectories:

- `win32` contains an [NSIS](http://nsis.sourceforge.net/) 3.0 installer script. To make it work for your purpose, just edit the constants under `; Configuration`.
- `osx` contains a [DMG Canvas](http://www.araelium.com/dmgcanvas) template. You can open it up in the GUI editor to fit your needs.

License
-------
This release of Work in Progress as a whole will be licensed under the Creative Commons BY-NC-ND 4.0 license. Individual components of this release should be treated as such:

* Art (files in the `game/bgs`, `game/cgs`, `game/sprites`, `game/ui` and `game/vfx` directories) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Music (files in the `game/music` directory) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Sound effects (files in the `game/sfx` directory) are licensed, at your choice, under either the Creative Commons BY-NC-ND 4.0 license or the Creative Commons BY-NC 4.0 license.
* Writing (files in the `game/scripts` directory that involve dialogue) is released, at your choice, under the Creative Commons BY-NC-ND 4.0 or the Creative Commons BY-NC-SA 4.0 license.
* Code (top-level files in the `game` directory, files in the `game/lib` and `game/scripts` directories) is, at your choice, licensed under either the Creative Commons BY-NC-ND 4.0 or the BSD 3-Clause license.
    - The engine code, Ren'Py, is licensed under a variety of licenses for its subcomponents. See [this file](http://txt.shiz.me/YzBlZDBm.txt) for more details.

In addition to these licenses, we would like to make the following specific waivers to further define the wishes of our developers and allow:

* Art: The artwork (Sprites, CGs and background art) of Work in Progress is non-derivative and forbidden to be used in any works other than Work in Progress, except as set forth in the derivation waiver. However, fan-made artwork of characters is allowed, but has to released as-is for the enjoyment of others and not as part of another project or compound work, except as set forth in the derivation waiver. 
* Music: It is allowed to make direct remixes, sampling or remakes (further referred to as "derivative music") of Work in Progress' soundtrack, under the following conditions or the conditions of the derivation waiver.
    - Derivative music will not be released in other collaborative works, such as but not limited to: video games, visual novels, or other projects of any scope or scale.
    - Derivative music may be released as-is and as standalone songs (or albums) for the enjoyment of others. 

Furthermore, we would not like to impair your ability to modify Work in Progress itself to suit your individual needs or tastes. That is why we add the following waiver for both the entirety of this release and the individual components listed previously (from here on labeled "assets"):

Derivation waiver
-----------------
Any person(s) (further referred to as "end-user") who wishes to modify and redistribute modifications of the assets involved in Work in Progress (further referred to as "derivative work") are allowed to, providing they abide by the following conditions:

* No credit is claimed or implied by the end-user for assets made by those other than themselves. Note: Modifying any asset does not change who the original creator is. In order to assert that an asset is the end-user's, they must create it themselves. Additionally, creating an asset in the exact likeness of another does not entitle you to claim said asset as your own. Plagiarizing any pre-existing assets will not change ownership of said asset.
* Any derivative work must be transparent about the fact that it is a derivative work of Work in Progress and not claim to be anything else.
* Any derivative work must be transparent about the fact that it is not an official release of Work in Progress by Salty Salty Studios, and mark itself as such.
* All of of Work in Progress' original assets (modified or unmodified) will maintain their licenses and clauses when redistributed in a derivative work.

Both the derivative work and all the assets themselves should follow the terms both set forth in the Creative Commons BY-NC 4.0 license, this additional waiver, and be licensed under the Creative Commons BY-NC-ND 4.0 license WITH this waiver.

Support
-------
This release comes without any support, warranty or guarantee that your PC won't be set on fire. However, if you have any questions, you can drop by on IRC: `#workinprogress` on `irc.rizon.net`. You can also use the [webchat](https://blog.salty-salty-studios.com/irc). If someone is around they might be able to help you.
