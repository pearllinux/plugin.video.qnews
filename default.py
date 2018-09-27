# -*- coding: utf-8 -*-
#------------------------------------------------------------
# QNEWS Addon by SCOTTYVBAMA
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: SCOTTYVBAMA
# Twitter:  @scottyvbama
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon



addonID = 'plugin.video.qnews'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCesUpcSqTPRyUmDnQnnW14A"
YOUTUBE_CHANNEL_ID_2 = "UCGQ2Sr_tQ8YPbnfDHdKWRPw"
YOUTUBE_CHANNEL_ID_3 = "UC98Zwfvjq12M1oi99Yqd78w"
YOUTUBE_CHANNEL_ID_4 = "UCxz5R9YQMRW5QqElbAlMqRw"
YOUTUBE_CHANNEL_ID_5 = "UCDB5XReUyyqt-FTNdkzFN-A"
YOUTUBE_CHANNEL_ID_6 = "UC8VYbOH2Z_swlgSSQ-RwaUg"
YOUTUBE_CHANNEL_ID_7 = "SGTbull07"
YOUTUBE_CHANNEL_ID_8 = "UCMVTRzCXvIbdK0Y1ZxD-BlA"
YOUTUBE_CHANNEL_ID_9 = "TruthAndArtTV"
YOUTUBE_CHANNEL_ID_10 = "StormCloudsGathering"
YOUTUBE_CHANNEL_ID_11 = "LionelY2K"
YOUTUBE_CHANNEL_ID_12 = "UCwJq9pqEEUr5_OmwBWQxDKA"
YOUTUBE_CHANNEL_ID_13 = "UC3yCYDoc70dMMQGKL364wHQ"
YOUTUBE_CHANNEL_ID_14 = "UCSio3E7kYvPeHKhfuYZWriA"
YOUTUBE_CHANNEL_ID_15 = "UC5ot7kRfXVOe4DcX3RC6lcQ"
YOUTUBE_CHANNEL_ID_16 = "UCKpH2KFEngc9Csp2i71znYA"
YOUTUBE_CHANNEL_ID_17 = "UCo6yPvF48mks8D56pgU73kA"
YOUTUBE_CHANNEL_ID_18 = "UCDMkBheMOpkNYF6E9vO5icg"
YOUTUBE_CHANNEL_ID_19 = "UCJ5PQfYe6er4rrt4LLu7EKg"
YOUTUBE_CHANNEL_ID_20 = "UConWcy4YIDbrL3mSmVSIjzw"
YOUTUBE_CHANNEL_ID_21 = "UCpwXjOAwWDuWlmA2gTjjBwg"
YOUTUBE_CHANNEL_ID_22 = "UCYuTOagsxlfgVBfOzCjxOPw"
YOUTUBE_CHANNEL_ID_23 = "UCv_-yc055n1fxFfTYpdaKBg"
YOUTUBE_CHANNEL_ID_24 = "UCeYzEIqv7D2NT7tP8Yz1x9Q"
YOUTUBE_CHANNEL_ID_25 = "UC62KZJ1mShIQ-14rjzVYt9A"

# Entry point
def run():
    plugintools.log("qnews.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("qnews.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Trusted Real News",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Citizens Investigative Report",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Truth Will Never Lie",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Truth and Art TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="H.A. Goodman",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Face Like the Sun",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blessed To Teach",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Lionel Nation",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Tracy Beanz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Daily Trite",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="You Are Free TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="SGTreport",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="David Harris Jr.",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="T.R.U Reporting",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BPEarthWatch",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spaceshot76",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="A call for an Uprising",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Storm Clouds Gathering",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lori Colley",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Destroying the Illusion",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail=icon,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="CBTS Stream",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail=icon,
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="James Munder",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="We the People",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Patriot Hour",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Praying Medic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail=icon,
        folder=True ) 

xbmc.executebuiltin("Container.SetViewMode(500)")
run()
