from xbmcswift2 import Plugin, xbmcgui
from resources.lib import thisislove

plugin = Plugin()

# base url for fetching podcasts 
URL = "http://feeds.thisiscriminal.com/thisislovepodcast"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://thisislovepodcast.com/wp-content/uploads/2019/05/cropped-favicon-1-270x270.png"},
   {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://thisislovepodcast.com/wp-content/uploads/2019/05/cropped-favicon-1-270x270.png"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = thisislove.get_soup(URL)
    
    playable_podcast = thisislove.get_playable_podcast(soup)
    
    items = thisislove.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = thisislove.get_soup(URL)
    
    playable_podcast1 = thisislove.get_playable_podcast1(soup)
    
    items = thisislove.compile_playable_podcast1(playable_podcast1)

    return items

if __name__ == '__main__':
    plugin.run()
