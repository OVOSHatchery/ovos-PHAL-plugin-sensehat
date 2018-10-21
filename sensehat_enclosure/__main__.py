import sys
from mycroft.configuration.config import Configuration
from mycroft.util.log import LOG


def main():
    config = Configuration.get().get("enclosure", {})
    platform = config.get("platform", "linux").lower()
    if platform.lower().startswith("sense"):
        from sensehat_enclosure import SenseHatEnclosure
        enclosure = SenseHatEnclosure()

        try:
            enclosure.run()
        except Exception as e:
            LOG.error(e)
        finally:
            enclosure.shutdown()
            sys.exit()
    else:
        LOG.error("Config says im running in " + platform + ", sensehat "
                                                            "enclosure needed")


if __name__ == "__main__":
    main()
