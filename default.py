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
YOUTUBE_CHANNEL_ID_6 = "TheAlexJonesChannel"
YOUTUBE_CHANNEL_ID_7 = "SGTbull07"
YOUTUBE_CHANNEL_ID_8 = "UC0v4ZBPYfq-sPmXOd67cDww"
YOUTUBE_CHANNEL_ID_9 = "UCraPqmcydVU-tWsAM_vpUvg"
YOUTUBE_CHANNEL_ID_10 = "StormCloudsGathering"
YOUTUBE_CHANNEL_ID_11 = "LionelY2K"
YOUTUBE_CHANNEL_ID_12 = "UChD-zWutIego-bcHKOatFWA"
YOUTUBE_CHANNEL_ID_13 = "roypotterqa"
YOUTUBE_CHANNEL_ID_14 = "UCSio3E7kYvPeHKhfuYZWriA"
YOUTUBE_CHANNEL_ID_15 = "UC5ot7kRfXVOe4DcX3RC6lcQ"
YOUTUBE_CHANNEL_ID_16 = "UCWW3gYCvKS412p7o6qSK5gg"
YOUTUBE_CHANNEL_ID_17 = "UCw5pSFA1KVZJruigo_FVv2Q"
YOUTUBE_CHANNEL_ID_18 = "UCDMkBheMOpkNYF6E9vO5icg"
YOUTUBE_CHANNEL_ID_19 = "UCJ5PQfYe6er4rrt4LLu7EKg"
YOUTUBE_CHANNEL_ID_20 = "UConWcy4YIDbrL3mSmVSIjzw"
YOUTUBE_CHANNEL_ID_21 = "UCv0dEcvXLOf4ZFvjCahK4Lw"
YOUTUBE_CHANNEL_ID_22 = "UCYuTOagsxlfgVBfOzCjxOPw"
YOUTUBE_CHANNEL_ID_23 = "UCv_-yc055n1fxFfTYpdaKBg"
YOUTUBE_CHANNEL_ID_24 = "27TUBGUY"
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
        title="Qnews Temp Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alex Jones",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
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
        title="April LaJune",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
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
        title="Roy Potter",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
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
        title="Open Mind",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
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
        title="American Intelligence Media",
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
        title="Anti School",
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
        title="Richie From Boston",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
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
        title="AMTV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Praying Medic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail=icon,
        folder=True ) 

xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)

run()
