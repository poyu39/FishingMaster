from fishing_master import FishingMaster

if __name__ == '__main__':
    fm = FishingMaster()
    fm.start_listener()

    while True:
        fm.set_bar()
        fm.fishing()