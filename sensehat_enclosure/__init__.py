from sensehat_enclosure.mycroft_enclosure_template import EnclosureTemplate
from sense_hat import SenseHat


class SenseHatEnclosure(EnclosureTemplate):
    """
    This base class is intended to be used to interface with the hardware
    that is running Mycroft.  It exposes all possible commands which
    can be sent to a Mycroft enclosure implementation.

    This allows mycroft to interact with sensehat

    """

    def __init__(self, bus=None):
        """

        Args:
            bus: message bus client (optional)
        """
        EnclosureTemplate.__init__(self, bus, "SenseHat")
        # register any extra listeners here

        # do initial setup
        self.sense = SenseHat()

    def shutdown(self):
        """

        """
        EnclosureTemplate.shutdown(self)
        # unregister events here

        # perform any hardware shutdown

    def on_no_internet(self, message=None):
        """

        Args:
            message:
        """
        pass

    def record_begin(self, message=None):
        ''' listening started '''
        pass

    def record_end(self, message=None):
        ''' listening ended '''
        pass

    def talk_start(self, message=None):
        ''' speaking started '''
        pass

    def handle_awake(self, message=None):
        ''' handle wakeup animation '''
        pass

    def handle_sleep(self, message=None):
        ''' handle naptime animation '''
        # TODO naptime skill animation should be handled here
        pass

    def handle_speak(self, message=None):
        ''' handle speak messages, intended for enclosures that disregard
        visemes '''
        pass

    def reset(self, message=None):
        """The enclosure should restore itself to a started state.
        Typically this would be represented by the eyes being 'open'
        and the mouth reset to its default (smile or blank).
        """
        pass

    def system_reset(self, message=None):
        """The enclosure hardware should reset any CPUs, etc."""
        pass

    def system_mute(self, message=None):
        """Mute (turn off) the system speaker."""
        pass

    def system_unmute(self, message=None):
        """Unmute (turn on) the system speaker."""
        pass

    def system_blink(self, message=None):
        """The 'eyes' should blink the given number of times.
        Args:
            times (int): number of times to blink
        """
        pass

    def eyes_on(self, message=None):
        """Illuminate or show the eyes."""
        pass

    def eyes_off(self, message=None):
        """Turn off or hide the eyes."""
        pass

    def eyes_fill(self, message=None):
        pass

    def eyes_blink(self, message=None):
        """Make the eyes blink
        Args:
            side (str): 'r', 'l', or 'b' for 'right', 'left' or 'both'
        """
        pass

    def eyes_narrow(self, message=None):
        """Make the eyes look narrow, like a squint"""
        pass

    def eyes_look(self, message=None):
        """Make the eyes look to the given side
        Args:
            side (str): 'r' for right
                        'l' for left
                        'u' for up
                        'd' for down
                        'c' for crossed
        """
        pass

    def eyes_color(self, message=None):
        """Change the eye color to the given RGB color
        Args:
            r (int): 0-255, red value
            g (int): 0-255, green value
            b (int): 0-255, blue value
        """
        pass

    def eyes_brightness(self, message=None):
        """Set the brightness of the eyes in the display.
        Args:
            level (int): 1-30, bigger numbers being brighter
        """
        pass

    def eyes_reset(self, message=None):
        """Restore the eyes to their default (ready) state."""
        pass

    def eyes_timed_spin(self, message=None):
        """Make the eyes 'roll' for the given time.
        Args:
            length (int): duration in milliseconds of roll, None = forever
        """
        pass

    def eyes_volume(self, message=None):
        """Indicate the volume using the eyes
        Args:
            volume (int): 0 to 11
        """
        pass

    def eyes_spin(self, message=None):
        """
        Args:
        """
        pass

    def eyes_set_pixel(self, message=None):
        """
        Args:
        """
        pass

    def mouth_reset(self, message=None):
        """Restore the mouth display to normal (blank)"""
        pass

    def mouth_talk(self, message=None):
        """Show a generic 'talking' animation for non-synched speech"""
        pass

    def mouth_think(self, message=None):
        """Show a 'thinking' image or animation"""
        pass

    def mouth_listen(self, message=None):
        """Show a 'thinking' image or animation"""
        pass

    def mouth_smile(self, message=None):
        """Show a 'smile' image or animation"""
        pass

    def mouth_viseme(self, message=None):
        """Display a viseme mouth shape for synched speech
        Args:
            code (int):  0 = shape for sounds like 'y' or 'aa'
                         1 = shape for sounds like 'aw'
                         2 = shape for sounds like 'uh' or 'r'
                         3 = shape for sounds like 'th' or 'sh'
                         4 = neutral shape for no sound
                         5 = shape for sounds like 'f' or 'v'
                         6 = shape for sounds like 'oy' or 'ao'
        """
        pass

    def mouth_text(self, message=None):
        """Display text (scrolling as needed)
        Args:
            text (str): text string to display
        """
        pass

    def mouth_display(self, message=None):
        """Display images on faceplate. Currently supports images up to 16x8,
           or half the face. You can use the 'x' parameter to cover the other
           half of the faceplate.
        Args:
            img_code (str): text string that encodes a black and white image
            x (int): x offset for image
            y (int): y offset for image
            refresh (bool): specify whether to clear the faceplate before
                            displaying the new image or not.
                            Useful if you'd like to display muliple images
                            on the faceplate at once.
        """
        pass

    def weather_display(self, message=None):
        """Show a the temperature and a weather icon

        Args:
            img_code (char): one of the following icon codes
                         0 = sunny
                         1 = partly cloudy
                         2 = cloudy
                         3 = light rain
                         4 = raining
                         5 = stormy
                         6 = snowing
                         7 = wind/mist
            temp (int): the temperature (either C or F, not indicated)
        """
        pass

    def activate_mouth_events(self, message=None):
        """Enable movement of the mouth with speech"""
        pass

    def deactivate_mouth_events(self, message=None):
        """Disable movement of the mouth with speech"""
        pass


class FakeSkillSettings(object):
    """
    Mock settings class ensuring minimum syntax so it can be packaged as a
    skill
    """
    allow_overwrite = True

    @staticmethod
    def load_skill_settings_from_file():
        pass

    @staticmethod
    def get(k="", defaul=None):
        return False  # disable first run conditional on load


class SenseHatSkill(object):
    """
        Mock skill class ensuring minimum syntax so it can be packaged as a
        skill and get the ws object on load
        """
    skill_id = "fake"
    settings = FakeSkillSettings

    sense = None

    @staticmethod
    def bind(bus):
        if SenseHatSkill.sense is None:
            SenseHatSkill.sense = SenseHatEnclosure(bus)

    @staticmethod
    def initialize():
        pass

    @staticmethod
    def _register_decorated():
        pass

    @staticmethod
    def load_data_files(path):
        pass

    @staticmethod
    def defult_shutdown():
        pass


def create_skill():
    return SenseHatSkill()
