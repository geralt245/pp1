class TV:

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 9

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if len(self.channels) == 0 or self.channel_no > len(self.channels) or self.channel_no < 0:
            return

        channel_name = self.channels[self.channel_no - 1]

        if self.is_on == True:
            print(f"TV is on, channel {self.channel_no} ({channel_name})")
            print(f"Volume {self.volume}")
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        for i in range(0, len(self.channels)):
            print(f"{i + 1}. {self.channels[i]}")

    def increase_volume(self):
        new_volume = self.volume + 1

        if new_volume >= 0 and new_volume <= 10:
            self.volume = new_volume

    def decrease_volume(self):
        new_volume = self.volume - 1

        if new_volume >= 0 and new_volume <= 10:
            self.volume = new_volume
