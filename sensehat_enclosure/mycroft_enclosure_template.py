import time
from threading import Thread
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
from mycroft.util.log import LOG


class EnclosureTemplate(object):
    """
    This base class is intended to be used to interface with the hardware
    that is running Mycroft.  It exposes all possible commands which
    can be sent to a Mycroft enclosure implementation.


    """

    def __init__(self, bus=None, name=""):
        """

        Args:
            bus:
            name:
        """
        if bus is None:
            self.bus = WebsocketClient()
            self.event_thread = Thread(target=self._connect)
            self.event_thread.setDaemon(True)
            self.event_thread.start()
        else:
            self.bus = bus
        self.log = LOG
        self.name = name
        self.bus.on("open", self.on_ws_open)
        self.bus.on("enclosure.reset", self.reset)
        # enclosure commands for Mycroft's Hardware.
        self.bus.on("enclosure.system.reset", self.system_reset)
        self.bus.on("enclosure.system.mute", self.system_mute)
        self.bus.on("enclosure.system.unmute", self.system_unmute)
        self.bus.on("enclosure.system.blink", self.system_blink)
        # enclosure commands for eyes
        self.bus.on('enclosure.eyes.on', self.eyes_on)
        self.bus.on('enclosure.eyes.off', self.eyes_off)
        self.bus.on('enclosure.eyes.blink', self.eyes_blink)
        self.bus.on('enclosure.eyes.narrow', self.eyes_narrow)
        self.bus.on('enclosure.eyes.look', self.eyes_look)
        self.bus.on('enclosure.eyes.color', self.eyes_color)
        self.bus.on('enclosure.eyes.level', self.eyes_brightness)
        self.bus.on('enclosure.eyes.volume', self.eyes_volume)
        self.bus.on('enclosure.eyes.spin', self.eyes_spin)
        self.bus.on('enclosure.eyes.timedspin', self.eyes_timed_spin)
        self.bus.on('enclosure.eyes.reset', self.eyes_reset)
        self.bus.on('enclosure.eyes.setpixel', self.eyes_set_pixel)
        self.bus.on('enclosure.eyes.fill', self.eyes_fill)

        # enclosure commands for mouth
        self.bus.on("enclosure.mouth.reset", self.mouth_reset)
        self.bus.on("enclosure.mouth.talk", self.mouth_talk)
        self.bus.on("enclosure.mouth.think", self.mouth_think)
        self.bus.on("enclosure.mouth.listen", self.mouth_listen)
        self.bus.on("enclosure.mouth.smile", self.mouth_smile)
        self.bus.on("enclosure.mouth.viseme", self.mouth_viseme)
        self.bus.on("enclosure.mouth.text", self.mouth_text)
        self.bus.on("enclosure.mouth.display", self.mouth_display)
        self.bus.on("enclosure.mouth.events.activate",
                    self.activate_mouth_events)
        self.bus.on("enclosure.mouth.events.deactivate",
                    self.deactivate_mouth_events)
        # enclosure commands for weather display
        self.bus.on("enclosure.weather.display", self.weather_display)
        # enclosure commands for events
        self.bus.on("mycroft.awoken", self.handle_awake)
        self.bus.on("recognizer_loop:sleep", self.handle_sleep)
        self.bus.on("speak", self.handle_speak)
        self.bus.on('recognizer_loop:record_begin', self.record_begin)
        self.bus.on('recognizer_loop:record_end', self.record_end)
        self.bus.on('mycroft.audio.speech.start', self.talk_start)
        self.bus.on("enclosure.notify.no_internet", self.on_no_internet)
        self.activate_mouth_events()

    def shutdown(self):
        """

        """
        self.bus.remove("enclosure.reset", self.reset)
        self.bus.remove("enclosure.system.reset", self.system_reset)
        self.bus.remove("enclosure.system.mute", self.system_mute)
        self.bus.remove("enclosure.system.unmute", self.system_unmute)
        self.bus.remove("enclosure.system.blink", self.system_blink)

        self.bus.remove("enclosure.eyes.on", self.eyes_on)
        self.bus.remove("enclosure.eyes.off", self.eyes_off)
        self.bus.remove("enclosure.eyes.blink", self.eyes_blink)
        self.bus.remove("enclosure.eyes.narrow", self.eyes_narrow)
        self.bus.remove("enclosure.eyes.look", self.eyes_look)
        self.bus.remove("enclosure.eyes.color", self.eyes_color)
        self.bus.remove("enclosure.eyes.brightness", self.eyes_brightness)
        self.bus.remove("enclosure.eyes.reset", self.eyes_reset)
        self.bus.remove("enclosure.eyes.timedspin", self.eyes_timed_spin)
        self.bus.remove("enclosure.eyes.volume", self.eyes_volume)
        self.bus.remove("enclosure.eyes.spin", self.eyes_spin)
        self.bus.remove("enclosure.eyes.set_pixel", self.eyes_set_pixel)

        self.bus.remove("enclosure.mouth.reset", self.mouth_reset)
        self.bus.remove("enclosure.mouth.talk", self.mouth_talk)
        self.bus.remove("enclosure.mouth.think", self.mouth_think)
        self.bus.remove("enclosure.mouth.listen", self.mouth_listen)
        self.bus.remove("enclosure.mouth.smile", self.mouth_smile)
        self.bus.remove("enclosure.mouth.viseme", self.mouth_viseme)
        self.bus.remove("enclosure.mouth.text", self.mouth_text)
        self.bus.remove("enclosure.mouth.display", self.mouth_display)
        self.bus.remove("enclosure.mouth.events.activate",
                        self.activate_mouth_events)
        self.bus.remove("enclosure.mouth.events.deactivate",
                        self.deactivate_mouth_events)

        self.bus.remove("enclosure.weather.display", self.weather_display)

        self.bus.remove("mycroft.awoken", self.handle_awake)
        self.bus.remove("recognizer_loop:sleep", self.handle_sleep)
        self.bus.remove("speak", self.handle_speak)
        self.bus.remove('recognizer_loop:record_begin', self.record_begin)
        self.bus.remove('recognizer_loop:record_end', self.record_end)
        self.bus.remove('recognizer_loop:audio_output_start', self.talk_start)
        self.bus.remove("enclosure.notify.no_internet", self.on_no_internet)
        self.deactivate_mouth_events()

    def on_no_internet(self, message=None):
        """

        Args:
            message:
        """
        pass

    def on_ws_open(self):
        """

        """
        pass

    def speak(self, text):
        """

        Args:
            text:
        """
        self.bus.emit(Message("speak", {'utterance': text}))

    def run(self):
        ''' start enclosure '''
        while True:
            time.sleep(1)

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

    def _connect(self):
        """

        """
        # Once the websocket has connected, just watch it for speak events
        self.bus.run_forever()

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


