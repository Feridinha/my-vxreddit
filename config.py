import configparser
import os

currentConfig = configparser.ConfigParser()

## default values

currentConfig["MAIN"]={
    "appName": "vxReddit",
    "embedColor": "#EE1D52",
    "repoURL":"https://github.com/dylanpdx/vxReddit",
    "domainName":"127.0.0.1:5000",
    "videoConversion":"local",
    "urlProtocol": "http://"
}

if 'RUNNING_SERVERLESS' in os.environ and os.environ['RUNNING_SERVERLESS'] == '1':
    urlProtocol = os.environ.get('URL_PROTOCOL', 'https://')
    if "://" not in urlProtocol:
        urlProtocol = urlProtocol.rstrip(":") + "://"
    currentConfig["MAIN"]={
        "appName": os.environ['APP_NAME'],
        "embedColor": "#EE1D52",
        "repoURL":os.environ['REPO_URL'],
        "domainName":os.environ['DOMAINNAME'],
        "videoConversion":os.environ['VIDEOCONVERSION'],
        "urlProtocol": urlProtocol,
    }
else:
    if os.path.exists("vxReddit.conf"):
        # as per python docs, "the most recently added configuration has the highest priority"
        # "conflicting keys are taken from the more recent configuration while the previously existing keys are retained"
        currentConfig.read("vxReddit.conf")

    # Garante que urlProtocol sempre tenha :// (ex: "http" -> "http://")
    urlProtocol = currentConfig["MAIN"].get("urlProtocol", "http://")
    if "://" not in urlProtocol:
        urlProtocol = urlProtocol.rstrip(":") + "://"
    currentConfig["MAIN"]["urlProtocol"] = urlProtocol

    with open("vxReddit.conf", "w") as configfile:
        currentConfig.write(configfile) # write current config to file