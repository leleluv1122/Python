from TV import TV

def main():
    tv1 = TV()
    tv1.turnon()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2 = TV()
    tv2.turnon()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1's channel is", tv1.getChannel(), "and volumelevel is", tv1.getVolumeLevl())
    print("tv2's channel is", tv2.getChannel(), "and volumelevel is", tv2.getVolumeLevl())

main()