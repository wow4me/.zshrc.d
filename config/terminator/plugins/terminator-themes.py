import requests
import terminatorlib.plugin as plugin
from gi.repository import Gtk, Gdk
from terminatorlib.config import ConfigBase
from terminatorlib.translation import _
from terminatorlib.util import get_config_dir, err, dbg, gerr

AVAILABLE = ['TerminatorThemes']

themes = [{
    "name": "3024 Day",
    "palette":
    "#090300:#db2d20:#01a252:#fded02:#01a0e4:#a16a94:#b5e4f4:#a5a2a2:#5c5855:#e8bbd0:#3a3432:#4a4543:#807d7c:#d6d5d4:#cdab53:#f7f7f7",
    "background_color": "#f7f7f7",
    "cursor_color": "#4a4543",
    "foreground_color": "#4a4543",
    "background_image": "None",
    "type": "light"
}, {
    "name": "3024 Night",
    "palette":
    "#090300:#db2d20:#01a252:#fded02:#01a0e4:#a16a94:#b5e4f4:#a5a2a2:#5c5855:#e8bbd0:#3a3432:#4a4543:#807d7c:#d6d5d4:#cdab53:#f7f7f7",
    "background_color": "#090300",
    "cursor_color": "#a5a2a2",
    "foreground_color": "#a5a2a2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Aci",
    "background_color": "#0d1926",
    "background_image": "None",
    "cursor_color": "#c4e9ff",
    "foreground_color": "#b4e1fd",
    "palette":
    "#363636:#ff0883:#83ff08:#ff8308:#0883ff:#8308ff:#08ff83:#b6b6b6:#363636:#ff0883:#83ff08:#ff8308:#0883ff:#8308ff:#08ff83:#b6b6b6",
    "type": "dark"
}, {
    "name": "Aco",
    "background_color": "#1f1305",
    "background_image": "None",
    "cursor_color": "#bae2fb",
    "foreground_color": "#b4e1fd",
    "palette":
    "#3f3f3f:#ff0883:#83ff08:#ff8308:#0883ff:#8308ff:#08ff83:#bebebe:#474747:#ff1e8e:#8eff1e:#ff8e1e:#0883ff:#8e1eff:#1eff8e:#c4c4c4",
    "type": "dark"
}, {
    "name": "AdventureTime",
    "palette":
    "#050404:#bd0013:#4ab118:#e7741e:#0f4ac6:#665993:#70a598:#f8dcc0:#4e7cbf:#fc5f5a:#9eff6e:#efc11a:#1997c6:#9b5953:#c8faf4:#f6f5fb",
    "background_color": "#1f1d45",
    "cursor_color": "#efbf38",
    "foreground_color": "#f8dcc0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "After Dark",
    "background_color": "#10111b",
    "cursor_color": "#aaaaaa",
    "palette":
    "#2e3436:#ef4a9e:#00d2bc:#e7ca7a:#9399fa:#ca5bcc:#86d079:#d3d7cf:#555753:#ef4a9e:#00d2bc:#e7ca7a:#9399fa:#ca5bcc:#86d079:#eeeeec",
    "type": "dark"
}, {
    "name": "Afterglow",
    "palette":
    "#151515:#ac4142:#7e8e50:#e5b567:#6c99bb:#9f4e85:#7dd6cf:#d0d0d0:#505050:#ac4142:#7e8e50:#e5b567:#6c99bb:#9f4e85:#7dd6cf:#f5f5f5",
    "background_color": "#212121",
    "cursor_color": "#d0d0d0",
    "foreground_color": "#d0d0d0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "AlienBlood",
    "palette":
    "#112616:#7f2b27:#2f7e25:#717f24:#2f6a7f:#47587f:#327f77:#647d75:#3c4812:#e08009:#18e000:#bde000:#00aae0:#0058e0:#00e0c4:#73fa91",
    "background_color": "#0f1610",
    "cursor_color": "#73fa91",
    "foreground_color": "#637d75",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Argonaut",
    "palette":
    "#232323:#ff000f:#8ce10b:#ffb900:#008df8:#6d43a6:#00d8eb:#ffffff:#444444:#ff2740:#abe15b:#ffd242:#0092ff:#9a5feb:#67fff0:#ffffff",
    "background_color": "#0e1019",
    "cursor_color": "#ff0018",
    "foreground_color": "#fffaf4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Arthur",
    "palette":
    "#3d352a:#cd5c5c:#86af80:#e8ae5b:#6495ed:#deb887:#b0c4de:#bbaa99:#554444:#cc5533:#88aa22:#ffa75d:#87ceeb:#996600:#b0c4de:#ddccbb",
    "background_color": "#1c1c1c",
    "cursor_color": "#e2bbef",
    "foreground_color": "#ddeedd",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "AtelierSulphurpool",
    "palette":
    "#202746:#c94922:#ac9739:#c08b30:#3d8fd1:#6679cc:#22a2c9:#979db4:#6b7394:#c76b29:#293256:#5e6687:#898ea4:#dfe2f1:#9c637a:#f5f7ff",
    "background_color": "#202746",
    "cursor_color": "#979db4",
    "foreground_color": "#979db4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Atom",
    "palette":
    "#000000:#fd5ff1:#87c38a:#ffd7b1:#85befd:#b9b6fc:#85befd:#e0e0e0:#000000:#fd5ff1:#94fa36:#f5ffa8:#96cbfe:#b9b6fc:#85befd:#e0e0e0",
    "background_color": "#161719",
    "cursor_color": "#d0d0d0",
    "foreground_color": "#c5c8c6",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "AtomOneLight",
    "palette":
    "#000000:#de3e35:#3f953a:#d2b67c:#2f5af3:#950095:#3f953a:#bbbbbb:#000000:#de3e35:#3f953a:#d2b67c:#2f5af3:#a00095:#3f953a:#ffffff",
    "background_color": "#f9f9f9",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#2a2c33",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Aurora",
    "background_color": "#0f1c21",
    "cursor_color": "#00485a",
    "foreground_color": "#80b6ad",
    "palette":
    "#0f1c21:#046655:#04c975:#b5bd68:#308891:#94a5bc:#8abeb7:#80b6ad:#0f1c21:#046655:#04c975:#b5bd68:#308891:#94a5bc:#8abeb7:#80b6ad",
    "type": "dark"
}, {
    "name": "ayu",
    "palette":
    "#000000:#ff3333:#b8cc52:#e7c547:#36a3d9:#f07178:#95e6cb:#ffffff:#323232:#ff6565:#eafe84:#fff779:#68d5ff:#ffa3aa:#c7fffd:#ffffff",
    "background_color": "#0f1419",
    "cursor_color": "#f29718",
    "foreground_color": "#e6e1cf",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ayu mirage",
    "background_color": "#212733",
    "background_image": "None",
    "cursor_color": "#FFD580",
    "foreground_color": "#d9d7ce",
    "palette":
    "#212733:#ff3333:#bae67e:#ffd580:#5ccfe6:#d4bfff:#5ccfe6:#3d4752:#3e4b59:#ff3333:#bae67e:#ffd580:#5ccfe6:#d4bfff:#5ccfe6:#eeeeec",
    "type": "dark"
}, {
    "name": "ayu_light",
    "palette":
    "#000000:#ff3333:#86b300:#f29718:#41a6d9:#f07178:#4dbf99:#ffffff:#323232:#ff6565:#b8e532:#ffc94a:#73d8ff:#ffa3aa:#7ff1cb:#ffffff",
    "background_color": "#fafafa",
    "cursor_color": "#ff6a00",
    "foreground_color": "#5c6773",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Azu",
    "background_color": "#09111a",
    "background_image": "None",
    "cursor_color": "#d2e8fc",
    "foreground_color": "#d9e6f2",
    "palette":
    "#000000:#ac6d74:#74ac6d:#aca46d:#6d74ac:#a46dac:#6daca4:#e6e6e6:#262626:#d6b8bc:#bcd6b8:#d6d3b8:#b8bcd6:#d3b8d6:#b8d6d3:#ffffff",
    "type": "dark"
}, {
    "name": "Batman",
    "palette":
    "#1b1d1e:#e6dc44:#c8be46:#f4fd22:#737174:#747271:#62605f:#c6c5bf:#505354:#fff78e:#fff27d:#feed6c:#919495:#9a9a9d:#a3a3a6:#dadbd6",
    "background_color": "#1b1d1e",
    "cursor_color": "#fcef0c",
    "foreground_color": "#6f6f6f",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Belafonte Day",
    "palette":
    "#20111b:#be100e:#858162:#eaa549:#426a79:#97522c:#989a9c:#968c83:#5e5252:#be100e:#858162:#eaa549:#426a79:#97522c:#989a9c:#d5ccba",
    "background_color": "#d5ccba",
    "cursor_color": "#45373c",
    "foreground_color": "#45373c",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Belafonte Night",
    "palette":
    "#20111b:#be100e:#858162:#eaa549:#426a79:#97522c:#989a9c:#968c83:#5e5252:#be100e:#858162:#eaa549:#426a79:#97522c:#989a9c:#d5ccba",
    "background_color": "#20111b",
    "cursor_color": "#968c83",
    "foreground_color": "#968c83",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Bim",
    "background_color": "#012849",
    "background_image": "None",
    "cursor_color": "#c4d0de",
    "foreground_color": "#a9bed8",
    "palette":
    "#2c2423:#f557a0:#a9ee55:#f5a255:#5ea2ec:#a957ec:#5eeea0:#918988:#918988:#f579b2:#bbee78:#f5b378:#81b3ec:#bb79ec:#81eeb2:#f5eeec",
    "type": "dark"
}, {
    "name": "BirdsOfParadise",
    "palette":
    "#573d26:#be2d26:#6ba18a:#e99d2a:#5a86ad:#ac80a6:#74a6ad:#e0dbb7:#9b6c4a:#e84627:#95d8ba:#d0d150:#b8d3ed:#d19ecb:#93cfd7:#fff9d5",
    "background_color": "#2a1f1d",
    "cursor_color": "#573d26",
    "foreground_color": "#e0dbb7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Blazer",
    "palette":
    "#000000:#b87a7a:#7ab87a:#b8b87a:#7a7ab8:#b87ab8:#7ab8b8:#d9d9d9:#262626:#dbbdbd:#bddbbd:#dbdbbd:#bdbddb:#dbbddb:#bddbdb:#ffffff",
    "background_color": "#0d1926",
    "cursor_color": "#d9e6f2",
    "foreground_color": "#d9e6f2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Blitz",
    "background_color": "#16141e",
    "cursor_color": "#00ecc8",
    "foreground_color": "#00ecc8",
    "palette":
    "#2e3436:#f70047:#00ff7d:#fcdd42:#26b3d2:#b055f4:#ff8db4:#d3d7cf:#555753:#ff5555:#55ff55:#ffff55:#729fcf:#ff55ff:#34e2e2:#eeeeec",
    "type": "dark"
}, {
    "name": "Bloody",
    "background_color": "#1e1f29",
    "background_image": "None",
    "cursor_color": "#f9dc5c",
    "foreground_color": "#aaaaaa",
    "palette":
    "#2e3436:#ff512f:#b2ffa9:#fffd82:#3185fc:#dd2476:#66d7d1:#f2efea:#555753:#ff512f:#b2ffa9:#fffd82:#3185fc:#dd2476:#66d7d1:#f2efea",
    "type": "dark"
}, {
    "name": "Borland",
    "palette":
    "#4f4f4f:#ff6c60:#a8ff60:#ffffb6:#96cbfe:#ff73fd:#c6c5fe:#eeeeee:#7c7c7c:#ffb6b0:#ceffac:#ffffcc:#b5dcff:#ff9cfe:#dfdffe:#ffffff",
    "background_color": "#0000a4",
    "cursor_color": "#ffa560",
    "foreground_color": "#ffff4e",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Bright Lights",
    "palette":
    "#191919:#ff355b:#b7e876:#ffc251:#76d4ff:#ba76e7:#6cbfb5:#c2c8d7:#191919:#ff355b:#b7e876:#ffc251:#76d5ff:#ba76e7:#6cbfb5:#c2c8d7",
    "background_color": "#191919",
    "cursor_color": "#f34b00",
    "foreground_color": "#b3c9d7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Broadcast",
    "palette":
    "#000000:#da4939:#519f50:#ffd24a:#6d9cbe:#d0d0ff:#6e9cbe:#ffffff:#323232:#ff7b6b:#83d182:#ffff7c:#9fcef0:#ffffff:#a0cef0:#ffffff",
    "background_color": "#2b2b2b",
    "cursor_color": "#ffffff",
    "foreground_color": "#e6e1dc",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Brogrammer",
    "palette":
    "#1f1f1f:#f81118:#2dc55e:#ecba0f:#2a84d2:#4e5ab7:#1081d6:#d6dbe5:#d6dbe5:#de352e:#1dd361:#f3bd09:#1081d6:#5350b9:#0f7ddb:#ffffff",
    "background_color": "#131313",
    "cursor_color": "#b9b9b9",
    "foreground_color": "#d6dbe5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "C64",
    "palette":
    "#090300:#883932:#55a049:#bfce72:#40318d:#8b3f96:#67b6bd:#ffffff:#000000:#883932:#55a049:#bfce72:#40318d:#8b3f96:#67b6bd:#f7f7f7",
    "background_color": "#40318d",
    "cursor_color": "#7869c4",
    "foreground_color": "#7869c4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Cai",
    "background_color": "#09111a",
    "background_image": "None",
    "cursor_color": "#e3eef9",
    "foreground_color": "#d9e6f2",
    "palette":
    "#000000:#ca274d:#4dca27:#caa427:#274dca:#a427ca:#27caa4:#808080:#808080:#e98da3:#a3e98d:#e9d48d:#8da3e9:#d48de9:#8de9d4:#ffffff",
    "type": "dark"
}, {
    "name": "Candy",
    "background_color": "#000000",
    "foreground_color": "#AAAAAA",
    "cursor_color": "#aaaaaa",
    "palette":
    "#2e3436:#fa2573:#a6e32d:#fc951e:#c48dff:#fa2573:#67d9f0:#f2f2f2:#555753:#fa2573:#8ae234:#fce94f:#729fcf:#fa2573:#34e2e2:#eeeeec",
    "type": "dark"
}, {
    "name": "Chalk",
    "palette":
    "#7d8b8f:#b23a52:#789b6a:#b9ac4a:#2a7fac:#bd4f5a:#44a799:#d2d8d9:#888888:#f24840:#80c470:#ffeb62:#4196ff:#fc5275:#53cdbd:#d2d8d9",
    "background_color": "#2b2d2e",
    "cursor_color": "#708284",
    "foreground_color": "#d2d8d9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Chalkboard",
    "palette":
    "#000000:#c37372:#72c373:#c2c372:#7372c3:#c372c2:#72c2c3:#d9d9d9:#323232:#dbaaaa:#aadbaa:#dadbaa:#aaaadb:#dbaada:#aadadb:#ffffff",
    "background_color": "#29262f",
    "cursor_color": "#d9e6f2",
    "foreground_color": "#d9e6f2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Chalkby",
    "background_color": "#1f2d2d",
    "cursor_color": "#ffffff",
    "cursor_color_fg": "False",
    "foreground_color": "#ffffff",
    "palette":
    "#2e3436:#ffb0b0:#c8ff9b:#fffca4:#6f9ceb:#9395d3:#bdeaff:#d3d7cf:#555753:#ffb0b0:#c8ff9b:#fffca4:#6f9ceb:#9395d3:#bdeaff:#eeeeec",
    "type": "dark"
}, {
    "name": "Chesterish",
    "background_color": "#293340",
    "background_image": "None",
    "cursor_color": "#2c85f7",
    "foreground_color": "#cdd2e9",
    "palette":
    "#293340:#e17e85:#61ba86:#ffec8e:#4cb2ff:#be86e3:#2dced0:#cdd2e9:#546386:#e17e85:#61ba86:#ffec8e:#4cb2ff:#be86e3:#2dced0:#cdd2e9",
    "type": "dark"
}, {
    "name": "Ciapre",
    "palette":
    "#181818:#810009:#48513b:#cc8b3f:#576d8c:#724d7c:#5c4f4b:#aea47f:#555555:#ac3835:#a6a75d:#dcdf7c:#3097c6:#d33061:#f3dbb2:#f4f4f4",
    "background_color": "#191c27",
    "cursor_color": "#92805b",
    "foreground_color": "#aea47a",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "CLRS",
    "palette":
    "#000000:#f8282a:#328a5d:#fa701d:#135cd0:#9f00bd:#33c3c1:#b3b3b3:#555753:#fb0416:#2cc631:#fdd727:#1670ff:#e900b0:#3ad5ce:#eeeeec",
    "background_color": "#ffffff",
    "cursor_color": "#6fd3fc",
    "foreground_color": "#262626",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Cobalt Neon",
    "palette":
    "#142631:#ff2320:#3ba5ff:#e9e75c:#8ff586:#781aa0:#8ff586:#ba46b2:#fff688:#d4312e:#8ff586:#e9f06d:#3c7dd2:#8230a7:#6cbc67:#8ff586",
    "background_color": "#142838",
    "cursor_color": "#c4206f",
    "foreground_color": "#8ff586",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Cobalt2",
    "palette":
    "#000000:#ff0000:#38de21:#ffe50a:#1460d2:#ff005d:#00bbbb:#bbbbbb:#555555:#f40e17:#3bd01d:#edc809:#5555ff:#ff55ff:#6ae3fa:#ffffff",
    "background_color": "#132738",
    "cursor_color": "#f0cc09",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "CrayonPonyFish",
    "palette":
    "#2b1b1d:#91002b:#579524:#ab311b:#8c87b0:#692f50:#e8a866:#68525a:#3d2b2e:#c5255d:#8dff57:#c8381d:#cfc9ff:#fc6cba:#ffceaf:#b0949d",
    "background_color": "#150707",
    "cursor_color": "#68525a",
    "foreground_color": "#68525a",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Dark Pastel",
    "palette":
    "#000000:#ff5555:#55ff55:#ffff55:#5555ff:#ff55ff:#55ffff:#bbbbbb:#555555:#ff5555:#55ff55:#ffff55:#5555ff:#ff55ff:#55ffff:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Darkside",
    "palette":
    "#000000:#e8341c:#68c256:#f2d42c:#1c98e8:#8e69c9:#1c98e8:#bababa:#000000:#e05a4f:#77b869:#efd64b:#387cd3:#957bbe:#3d97e2:#bababa",
    "background_color": "#222324",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bababa",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "deep",
    "palette":
    "#000000:#d70005:#1cd915:#d9bd26:#5665ff:#b052da:#50d2da:#e0e0e0:#535353:#fb0007:#22ff18:#fedc2b:#9fa9ff:#e09aff:#8df9ff:#ffffff",
    "background_color": "#090909",
    "cursor_color": "#d0d0d0",
    "foreground_color": "#cdcdcd",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Desert",
    "palette":
    "#4d4d4d:#ff2b2b:#98fb98:#f0e68c:#cd853f:#ffdead:#ffa0a0:#f5deb3:#555555:#ff5555:#55ff55:#ffff55:#87ceff:#ff55ff:#ffd700:#ffffff",
    "background_color": "#333333",
    "cursor_color": "#00ff00",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "DimmedMonokai",
    "palette":
    "#3a3d43:#be3f48:#879a3b:#c5a635:#4f76a1:#855c8d:#578fa4:#b9bcba:#888987:#fb001f:#0f722f:#c47033:#186de3:#fb0067:#2e706d:#fdffb9",
    "background_color": "#1f1f1f",
    "cursor_color": "#f83e19",
    "foreground_color": "#b9bcba",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "DotGov",
    "palette":
    "#191919:#bf091d:#3d9751:#f6bb34:#17b2e0:#7830b0:#8bd2ed:#ffffff:#191919:#bf091d:#3d9751:#f6bb34:#17b2e0:#7830b0:#8bd2ed:#ffffff",
    "background_color": "#262c35",
    "cursor_color": "#d9002f",
    "foreground_color": "#ebebeb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Dracula",
    "background_color": "#1e1f29",
    "background_image": "None",
    "cursor_color": "#aaaaaa",
    "foreground_color": "#f8f8f2",
    "palette":
    "#44475a:#ff5555:#50fa7b:#f1fa8c:#8be9fd:#bd93f9:#ff79c6:#94a3a5:#000000:#ff5555:#50fa7b:#f1fa8c:#8be9fd:#bd93f9:#ff79c6:#ffffff",
    "type": "dark"
}, {
    "name": "Duotone Dark",
    "palette":
    "#1f1d27:#d9393e:#2dcd73:#d9b76e:#ffc284:#de8d40:#2488ff:#b7a1ff:#353147:#d9393e:#2dcd73:#d9b76e:#ffc284:#de8d40:#2488ff:#eae5ff",
    "background_color": "#1f1d27",
    "cursor_color": "#ff9839",
    "foreground_color": "#b7a1ff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Earthsong",
    "palette":
    "#121418:#c94234:#85c54c:#f5ae2e:#1398b9:#d0633d:#509552:#e5c6aa:#675f54:#ff645a:#98e036:#e0d561:#5fdaff:#ff9269:#84f088:#f6f7ec",
    "background_color": "#292520",
    "cursor_color": "#f6f7ec",
    "foreground_color": "#e5c7a9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Elemental",
    "palette":
    "#3c3c30:#98290f:#479a43:#7f7111:#497f7d:#7f4e2f:#387f58:#807974:#555445:#e0502a:#61e070:#d69927:#79d9d9:#cd7c54:#59d599:#fff1e9",
    "background_color": "#22211d",
    "cursor_color": "#facb80",
    "foreground_color": "#807a74",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Elementary",
    "palette":
    "#242424:#d71c15:#5aa513:#fdb40c:#063b8c:#e40038:#2595e1:#efefef:#4b4b4b:#fc1c18:#6bc219:#fec80e:#0955ff:#fb0050:#3ea8fc:#8c00ec",
    "background_color": "#181818",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#efefef",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Elio",
    "background_color": "#041a3b",
    "background_image": "None",
    "cursor_color": "#fbfbfb",
    "foreground_color": "#f2f2f2",
    "palette":
    "#303030:#e1321a:#6ab017:#ffc005:#729FCF:#ec0048:#2aa7e7:#f2f2f2:#5d5d5d:#ff361e:#7bc91f:#ffd00a:#0071ff:#ff1d62:#4bb8fd:#a020f0",
    "type": "dark"
}, {
    "name": "ENCOM",
    "palette":
    "#000000:#9f0000:#008b00:#ffd000:#0081ff:#bc00ca:#008b8b:#bbbbbb:#555555:#ff0000:#00ee00:#ffff00:#0000ff:#ff00ff:#00cdcd:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#00a595",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Espresso",
    "palette":
    "#353535:#d25252:#a5c261:#ffc66d:#6c99bb:#d197d9:#bed6ff:#eeeeec:#535353:#f00c0c:#c2e075:#e1e48b:#8ab7d9:#efb5f7:#dcf4ff:#ffffff",
    "background_color": "#323232",
    "cursor_color": "#d6d6d6",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Espresso Libre",
    "palette":
    "#000000:#cc0000:#1a921c:#f0e53a:#0066ff:#c5656b:#06989a:#d3d7cf:#555753:#ef2929:#9aff87:#fffb5c:#43a8ed:#ff818a:#34e2e2:#eeeeec",
    "background_color": "#2a211c",
    "cursor_color": "#ffffff",
    "foreground_color": "#b8a898",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Fideloper",
    "palette":
    "#292f33:#cb1e2d:#edb8ac:#b7ab9b:#2e78c2:#c0236f:#309186:#eae3ce:#092028:#d4605a:#d4605a:#a86671:#7c85c4:#5c5db2:#819090:#fcf4df",
    "background_color": "#292f33",
    "cursor_color": "#d4605a",
    "foreground_color": "#dbdae0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "FirefoxDev",
    "palette":
    "#002831:#e63853:#5eb83c:#a57706:#359ddf:#d75cff:#4b73a2:#dcdcdc:#001e27:#e1003f:#1d9000:#cd9409:#006fc0:#a200da:#005794:#e2e2e2",
    "background_color": "#0e1011",
    "cursor_color": "#708284",
    "foreground_color": "#7c8fa4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Firewatch",
    "palette":
    "#585f6d:#d95360:#5ab977:#dfb563:#4d89c4:#d55119:#44a8b6:#e6e5ff:#585f6d:#d95360:#5ab977:#dfb563:#4c89c5:#d55119:#44a8b6:#e6e5ff",
    "background_color": "#1e2027",
    "cursor_color": "#f6f7ec",
    "foreground_color": "#9ba2b2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "FishTank",
    "palette":
    "#03073c:#c6004a:#acf157:#fecd5e:#525fb8:#986f82:#968763:#ecf0fc:#6c5b30:#da4b8a:#dbffa9:#fee6a9:#b2befa:#fda5cd:#a5bd86:#f6ffec",
    "background_color": "#232537",
    "cursor_color": "#fecd5e",
    "foreground_color": "#ecf0fe",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Flat",
    "palette":
    "#222d3f:#a82320:#32a548:#e58d11:#3167ac:#781aa0:#2c9370:#b0b6ba:#212c3c:#d4312e:#2d9440:#e5be0c:#3c7dd2:#8230a7:#35b387:#e7eced",
    "background_color": "#002240",
    "cursor_color": "#e5be0c",
    "foreground_color": "#2cc55d",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Flatland",
    "palette":
    "#1d1d19:#f18339:#9fd364:#f4ef6d:#5096be:#695abc:#d63865:#ffffff:#1d1d19:#d22a24:#a7d42c:#ff8949:#61b9d0:#695abc:#d63865:#ffffff",
    "background_color": "#1d1f21",
    "cursor_color": "#708284",
    "foreground_color": "#b8dbef",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Floraverse",
    "palette":
    "#08002e:#64002c:#5d731a:#cd751c:#1d6da1:#b7077e:#42a38c:#f3e0b8:#331e4d:#d02063:#b4ce59:#fac357:#40a4cf:#f12aae:#62caa8:#fff5db",
    "background_color": "#0e0d15",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#dbd1b9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "ForestBlue",
    "palette":
    "#333333:#f8818e:#92d3a2:#1a8e63:#8ed0ce:#5e468c:#31658c:#e2d8cd:#3d3d3d:#fb3d66:#6bb48d:#30c85a:#39a7a2:#7e62b3:#6096bf:#e2d8cd",
    "background_color": "#051519",
    "cursor_color": "#9e9ecb",
    "foreground_color": "#e2d8cd",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Freya",
    "background_color": "#252e32",
    "background_image": "None",
    "cursor_color": "#839496",
    "foreground_color": "#94a3a5",
    "palette":
    "#073642:#dc322f:#859900:#b58900:#268bd2:#ec0048:#2aa198:#94a3a5:#586e75:#cb4b16:#859900:#b58900:#268bd2:#d33682:#2aa198:#6c71c4",
    "type": "dark"
}, {
    "name": "FrontEndDelight",
    "palette":
    "#242526:#f8511b:#565747:#fa771d:#2c70b7:#f02e4f:#3ca1a6:#adadad:#5fac6d:#f74319:#74ec4c:#fdc325:#3393ca:#e75e4f:#4fbce6:#8c735b",
    "background_color": "#1b1c1d",
    "cursor_color": "#cdcdcd",
    "foreground_color": "#adadad",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "FunForrest",
    "palette":
    "#000000:#d6262b:#919c00:#be8a13:#4699a3:#8d4331:#da8213:#ddc265:#7f6a55:#e55a1c:#bfc65a:#ffcb1b:#7cc9cf:#d26349:#e6a96b:#ffeaa3",
    "background_color": "#251200",
    "cursor_color": "#e5591c",
    "foreground_color": "#dec165",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Galaxy",
    "palette":
    "#000000:#f9555f:#21b089:#fef02a:#589df6:#944d95:#1f9ee7:#bbbbbb:#555555:#fa8c8f:#35bb9a:#ffff55:#589df6:#e75699:#3979bc:#ffffff",
    "background_color": "#1d2837",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Github",
    "palette":
    "#3e3e3e:#970b16:#07962a:#f8eec7:#003e8a:#e94691:#89d1ec:#ffffff:#666666:#de0000:#87d5a2:#f1d007:#2e6cba:#ffa29f:#1cfafe:#ffffff",
    "background_color": "#f4f4f4",
    "cursor_color": "#3f3f3f",
    "foreground_color": "#3e3e3e",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Glacier",
    "palette":
    "#2e343c:#bd0f2f:#35a770:#fb9435:#1f5872:#bd2523:#778397:#ffffff:#404a55:#bd0f2f:#49e998:#fddf6e:#2a8bc1:#ea4727:#a0b6d3:#ffffff",
    "background_color": "#0c1115",
    "cursor_color": "#6c6c6c",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Grape",
    "palette":
    "#2d283f:#ed2261:#1fa91b:#8ddc20:#487df4:#8d35c9:#3bdeed:#9e9ea0:#59516a:#f0729a:#53aa5e:#b2dc87:#a9bcec:#ad81c2:#9de3eb:#a288f7",
    "background_color": "#171423",
    "cursor_color": "#a288f7",
    "foreground_color": "#9f9fa1",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Grass",
    "palette":
    "#000000:#bb0000:#00bb00:#e7b000:#0000a3:#950062:#00bbbb:#bbbbbb:#555555:#bb0000:#00bb00:#e7b000:#0000bb:#ff55ff:#55ffff:#ffffff",
    "background_color": "#13773d",
    "cursor_color": "#8c2800",
    "foreground_color": "#fff0a5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Gruvbox Dark",
    "palette":
    "#161819:#f73028:#aab01e:#f7b125:#719586:#c77089:#7db669:#faefbb:#7f7061:#be0f17:#868715:#cc881a:#377375:#a04b73:#578e57:#e6d4a3",
    "background_color": "#1e1e1e",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#e6d4a3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Halcyon",
    "background_color": "#171c28",
    "cursor_color": "#5ccfe6",
    "foreground_color": "#d7dce2",
    "palette":
    "#1d2433:#ef6b73:#bae67e:#ffd580:#6679a4:#c3a6ff:#5ccfe6:#d7dce2:#1d2433:#ef6b73:#bae67e:#ffd580:#6679a4:#c3a6ff:#5ccfe6:#d7dce2",
    "type": "dark"
}, {
    "name": "Hardcore",
    "palette":
    "#1b1d1e:#f92672:#a6e22e:#fd971f:#66d9ef:#9e6ffe:#5e7175:#ccccc6:#505354:#ff669d:#beed5f:#e6db74:#66d9ef:#9e6ffe:#a3babf:#f8f8f2",
    "background_color": "#121212",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#a0a0a0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Harper",
    "palette":
    "#010101:#f8b63f:#7fb5e1:#d6da25:#489e48:#b296c6:#f5bfd7:#a8a49d:#726e6a:#f8b63f:#7fb5e1:#d6da25:#489e48:#b296c6:#f5bfd7:#fefbea",
    "background_color": "#010101",
    "cursor_color": "#a8a49d",
    "foreground_color": "#a8a49d",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Hemisu dark",
    "background_image": "None",
    "cursor_color": "#BAFFAA",
    "foreground_color": "#FFFFFF",
    "palette":
    "#444444:#FF0054:#B1D630:#9D895E:#67BEE3:#B576BC:#569A9F:#EDEDED:#777777:#D65E75:#BAFFAA:#ECE1C8:#9FD3E5:#DEB3DF:#B6E0E5:#FFFFFF",
    "type": "dark"
}, {
    "name": "Hemisu light",
    "background_color": "#EFEFEF",
    "background_image": "None",
    "cursor_color": "#FF0054",
    "foreground_color": "#444444",
    "palette":
    "#777777:#FF0055:#739100:#503D15:#538091:#5B345E:#538091:#999999:#999999:#D65E76:#9CC700:#947555:#9DB3CD:#A184A4:#85B2AA:#BABABA",
    "type": "light"
}, {
    "name": "Highway",
    "palette":
    "#000000:#d00e18:#138034:#ffcb3e:#006bb3:#6b2775:#384564:#ededed:#5d504a:#f07e18:#b1d130:#fff120:#4fc2fd:#de0071:#5d504a:#ffffff",
    "background_color": "#222225",
    "cursor_color": "#e0d9b9",
    "foreground_color": "#ededed",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Hipster Green",
    "palette":
    "#000000:#b6214a:#00a600:#bfbf00:#246eb2:#b200b2:#00a6b2:#bfbfbf:#666666:#e50000:#86a93e:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#100b05",
    "cursor_color": "#23ff18",
    "foreground_color": "#84c138",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Homebrew",
    "palette":
    "#000000:#990000:#00a600:#999900:#0000b2:#b200b2:#00a6b2:#bfbfbf:#666666:#e50000:#00d900:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#000000",
    "cursor_color": "#23ff18",
    "foreground_color": "#00ff00",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Horizon",
    "palette":
    "#e9436f:#f9cbbe:#ffaf87:#27d796:#6c6f93:#fdf0ed:#fadad1:#b877db:#e95379:#fadad1:#fac29a:#09f7a0:#6c6f8a:#ffffff:#eddad1:#b88adb",
    "background_color": "#1c1e26",
    "cursor_color": "#e95379",
    "foreground_color": "#bbbbbb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Hurtado",
    "palette":
    "#575757:#ff1b00:#a5e055:#fbe74a:#496487:#fd5ff1:#86e9fe:#cbcccb:#262626:#d51d00:#a5df55:#fbe84a:#89beff:#c001c1:#86eafe:#dbdbdb",
    "background_color": "#000000",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#dbdbdb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Hybrid",
    "palette":
    "#2a2e33:#b84d51:#b3bf5a:#e4b55e:#6e90b0:#a17eac:#7fbfb4:#b5b9b6:#1d1f22:#8d2e32:#798431:#e58a50:#4b6b88:#6e5079:#4d7b74:#5a626a",
    "background_color": "#161719",
    "cursor_color": "#b7bcba",
    "foreground_color": "#b7bcba",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "IC_Green_PPL",
    "palette":
    "#1f1f1f:#fb002a:#339c24:#659b25:#149b45:#53b82c:#2cb868:#e0ffef:#032710:#a7ff3f:#9fff6d:#d2ff6d:#72ffb5:#50ff3e:#22ff71:#daefd0",
    "background_color": "#3a3d3f",
    "cursor_color": "#42ff58",
    "foreground_color": "#d9efd3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "IC_Orange_PPL",
    "palette":
    "#000000:#c13900:#a4a900:#caaf00:#bd6d00:#fc5e00:#f79500:#ffc88a:#6a4f2a:#ff8c68:#f6ff40:#ffe36e:#ffbe55:#fc874f:#c69752:#fafaff",
    "background_color": "#262626",
    "cursor_color": "#fc531d",
    "foreground_color": "#ffcb83",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "idleToes",
    "palette":
    "#323232:#d25252:#7fe173:#ffc66d:#4099ff:#f680ff:#bed6ff:#eeeeec:#535353:#f07070:#9dff91:#ffe48b:#5eb7f7:#ff9dff:#dcf4ff:#ffffff",
    "background_color": "#323232",
    "cursor_color": "#d6d6d6",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "IR_Black",
    "palette":
    "#4f4f4f:#fa6c60:#a8ff60:#fffeb7:#96cafe:#fa73fd:#c6c5fe:#efedef:#7b7b7b:#fcb6b0:#cfffab:#ffffcc:#b5dcff:#fb9cfe:#e0e0fe:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#808080",
    "foreground_color": "#f1f1f1",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Jackie Brown",
    "palette":
    "#2c1d16:#ef5734:#2baf2b:#bebf00:#246eb2:#d05ec1:#00acee:#bfbfbf:#666666:#e50000:#86a93e:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#2c1d16",
    "cursor_color": "#23ff18",
    "foreground_color": "#ffcc2f",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Japanesque",
    "palette":
    "#343935:#cf3f61:#7bb75b:#e9b32a:#4c9ad4:#a57fc4:#389aad:#fafaf6:#595b59:#d18fa6:#767f2c:#78592f:#135979:#604291:#76bbca:#b2b5ae",
    "background_color": "#1e1e1e",
    "cursor_color": "#edcf4f",
    "foreground_color": "#f7f6ec",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Jellybeans",
    "palette":
    "#929292:#e27373:#94b979:#ffba7b:#97bedc:#e1c0fa:#00988e:#dedede:#bdbdbd:#ffa1a1:#bddeab:#ffdca0:#b1d8f6:#fbdaff:#1ab2a8:#ffffff",
    "background_color": "#121212",
    "cursor_color": "#ffa560",
    "foreground_color": "#dedede",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "JetBrains Darcula",
    "palette":
    "#000000:#fa5355:#126e00:#c2c300:#4581eb:#fa54ff:#33c2c1:#adadad:#555555:#fb7172:#67ff4f:#ffff00:#6d9df1:#fb82ff:#60d3d1:#eeeeee",
    "background_color": "#202020",
    "cursor_color": "#ffffff",
    "foreground_color": "#adadad",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Juicy",
    "background_color": "#212121",
    "cursor_color": "#fcfcfc",
    "foreground_color": "#fcfcfc",
    "palette":
    "#2e3436:#ff0945:#1aff81:#fff64a:#2bf1ff:#7b68ee:#98f4ff:#d3d7cf:#555753:#ff0945:#1aff81:#fff64a:#2bf1ff:#7b68ee:#98f4ff:#eeeeec",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Kibble",
    "palette":
    "#4d4d4d:#c70031:#29cf13:#d8e30e:#3449d1:#8400ff:#0798ab:#e2d1e3:#5a5a5a:#f01578:#6ce05c:#f3f79e:#97a4f7:#c495f0:#68f2e0:#ffffff",
    "background_color": "#0e100a",
    "cursor_color": "#9fda9c",
    "foreground_color": "#f7f7f7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Later This Evening",
    "palette":
    "#2b2b2b:#d45a60:#afba67:#e5d289:#a0bad6:#c092d6:#91bfb7:#3c3d3d:#454747:#d3232f:#aabb39:#e5be39:#6699d6:#ab53d6:#5fc0ae:#c1c2c2",
    "background_color": "#222222",
    "cursor_color": "#424242",
    "foreground_color": "#959595",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Lavandula",
    "palette":
    "#230046:#7d1625:#337e6f:#7f6f49:#4f4a7f:#5a3f7f:#58777f:#736e7d:#372d46:#e05167:#52e0c4:#e0c386:#8e87e0:#a776e0:#9ad4e0:#8c91fa",
    "background_color": "#050014",
    "cursor_color": "#8c91fa",
    "foreground_color": "#736e7d",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "LiquidCarbon",
    "palette":
    "#000000:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#bccccc:#000000:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#bccccc",
    "background_color": "#303030",
    "cursor_color": "#ffffff",
    "foreground_color": "#afc2c2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "LiquidCarbonTransparent",
    "palette":
    "#000000:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#bccccc:#000000:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#bccccc",
    "background_color": "#000000",
    "cursor_color": "#ffffff",
    "foreground_color": "#afc2c2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "LiquidCarbonTransparentInverse",
    "palette":
    "#bccccd:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#000000:#ffffff:#ff3030:#559a70:#ccac00:#0099cc:#cc69c8:#7ac4cc:#000000",
    "background_color": "#000000",
    "cursor_color": "#ffffff",
    "foreground_color": "#afc2c2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Lucy",
    "background_color": "#1a1b23",
    "cursor_color": "#af98e6",
    "foreground_color": "#96979b",
    "palette":
    "#2e3436:#fb7da7:#76c5a4:#e8d56d:#3465a4:#af98e6:#56c9db:#d3d7cf:#555753:#fb7da7:#76c5a4:#e8d56d:#729fcf:#af98e6:#56c9db:#eeeeec",
    "type": "dark"
}, {
    "name": "Man Page",
    "palette":
    "#000000:#cc0000:#00a600:#999900:#0000b2:#b200b2:#00a6b2:#cccccc:#666666:#e50000:#00d900:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#fef49c",
    "cursor_color": "#7f7f7f",
    "foreground_color": "#000000",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Mar",
    "background_color": "#ffffff",
    "background_image": "None",
    "cursor_color": "#23476a",
    "foreground_color": "#23476a",
    "palette":
    "#000000:#b5407b:#7bb540:#b57b40:#407bb5:#7b40b5:#40b57b:#f8f8f8:#737373:#cd73a0:#a0cd73:#cda073:#73a0cd:#a073cd:#73cda0:#ffffff",
    "type": "light"
}, {
    "name": "Material",
    "palette":
    "#212121:#b7141f:#457b24:#f6981e:#134eb2:#560088:#0e717c:#efefef:#424242:#e83b3f:#7aba3a:#ffea2e:#54a4f3:#aa4dbc:#26bbd1:#d9d9d9",
    "background_color": "#eaeaea",
    "cursor_color": "#16afca",
    "foreground_color": "#232322",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Material colors",
    "background_color": "#1E282C",
    "background_image": "None",
    "cursor_color": "#657B83",
    "foreground_color": "#C3C7D1",
    "palette":
    "#073641:#EB606B:#C3E88D:#F7EB95:#80CBC3:#FF2490:#AEDDFF:#FFFFFF:#002B36:#EB606B:#C3E88D:#F7EB95:#7DC6BF:#6C71C3:#34434D:#FFFFFF",
    "type": "dark"
}, {
    "name": "Material-Ocean",
    "background_color": "#0f111a",
    "cursor_color": "#ffcc00",
    "cursor_color_fg": "False",
    "foreground_color": "#8f93a2",
    "palette":
    "#2e3436:#ff5370:#c3e88d:#ffcb6b:#82aaff:#c792ea:#89ddff:#d3d7cf:#555753:#f07178:#c3e88d:#f78c6c:#729fcf:#bb80b3:#89ddff:#eeeeec",
    "type": "dark"
}, {
    "name": "Material-Palenight",
    "background_color": "#292d3e",
    "cursor_color": "#ffcc00",
    "cursor_color_fg": "False",
    "foreground_color": "#a6accd",
    "palette":
    "#2e3436:#ff5370:#c3e88d:#ffcb6b:#82aaff:#c792ea:#89ddff:#d3d7cf:#555753:#f07178:#c3e88d:#f78c6c:#729fcf:#bb80b3:#89ddff:#eeeeec",
    "type": "dark"
}, {
    "name": "MaterialDark",
    "palette":
    "#212121:#b7141f:#457b24:#f6981e:#134eb2:#560088:#0e717c:#efefef:#424242:#e83b3f:#7aba3a:#ffea2e:#54a4f3:#aa4dbc:#26bbd1:#d9d9d9",
    "background_color": "#232322",
    "cursor_color": "#16afca",
    "foreground_color": "#e5e5e5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Mathias",
    "palette":
    "#000000:#e52222:#a6e32d:#fc951e:#c48dff:#fa2573:#67d9f0:#f2f2f2:#555555:#ff5555:#55ff55:#ffff55:#5555ff:#ff55ff:#55ffff:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bbbbbb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Medallion",
    "palette":
    "#000000:#b64c00:#7c8b16:#d3bd26:#616bb0:#8c5a90:#916c25:#cac29a:#5e5219:#ff9149:#b2ca3b:#ffe54a:#acb8ff:#ffa0ff:#ffbc51:#fed698",
    "background_color": "#1d1908",
    "cursor_color": "#d3ba30",
    "foreground_color": "#cac296",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Misterioso",
    "palette":
    "#000000:#ff4242:#74af68:#ffad29:#338f86:#9414e6:#23d7d7:#e1e1e0:#555555:#ff3242:#74cd68:#ffb929:#23d7d7:#ff37ff:#00ede1:#ffffff",
    "background_color": "#2d3743",
    "cursor_color": "#000000",
    "foreground_color": "#e1e1e0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Miu",
    "background_color": "#0d1926",
    "background_image": "None",
    "cursor_color": "#d7dee4",
    "foreground_color": "#d9e6f2",
    "palette":
    "#000000:#b87a7a:#7ab87a:#b8b87a:#7a7ab8:#b87ab8:#7ab8b8:#d9d9d9:#262626:#dbbdbd:#bddbbd:#dbdbbd:#bdbddb:#dbbddb:#bddbdb:#ffffff",
    "type": "dark"
}, {
    "name": "Molokai",
    "palette":
    "#121212:#fa2573:#98e123:#dfd460:#1080d0:#8700ff:#43a8d0:#bbbbbb:#555555:#f6669d:#b1e05f:#fff26d:#00afff:#af87ff:#51ceff:#ffffff",
    "background_color": "#121212",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bbbbbb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "MonaLisa",
    "palette":
    "#351b0e:#9b291c:#636232:#c36e28:#515c5d:#9b1d29:#588056:#f7d75c:#874228:#ff4331:#b4b264:#ff9566:#9eb2b4:#ff5b6a:#8acd8f:#ffe598",
    "background_color": "#120b0d",
    "cursor_color": "#c46c32",
    "foreground_color": "#f7d66a",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Monokai dark",
    "background_color": "#272822",
    "background_image": "None",
    "cursor_color": "#ffffff",
    "foreground_color": "#f8f8f2",
    "palette":
    "#75715e:#f92672:#a6e22e:#f4bf75:#66d9ef:#ae81ff:#2aa198:#f9f8f5:#272822:#f92672:#a6e22e:#f4bf75:#66d9ef:#ae81ff:#2aa198:#f9f8f5",
    "type": "dark"
}, {
    "name": "Monokai Soda",
    "palette":
    "#1a1a1a:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#c4c5b5:#625e4c:#f4005f:#98e024:#e0d561:#9d65ff:#f4005f:#58d1eb:#f6f6ef",
    "background_color": "#1a1a1a",
    "cursor_color": "#f6f7ec",
    "foreground_color": "#c4c5b5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Monokai Vivid",
    "palette":
    "#121212:#fa2934:#98e123:#fff30a:#0443ff:#f800f8:#01b6ed:#ffffff:#838383:#f6669d:#b1e05f:#fff26d:#0443ff:#f200f6:#51ceff:#ffffff",
    "background_color": "#121212",
    "cursor_color": "#fb0007",
    "foreground_color": "#f9f9f9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "N0tch2k",
    "palette":
    "#383838:#a95551:#666666:#a98051:#657d3e:#767676:#c9c9c9:#d0b8a3:#474747:#a97775:#8c8c8c:#a99175:#98bd5e:#a3a3a3:#dcdcdc:#d8c8bb",
    "background_color": "#222222",
    "cursor_color": "#aa9175",
    "foreground_color": "#a0a0a0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Nebula",
    "background_color": "#23262e",
    "cursor_color": "#00e8c6",
    "foreground_color": "#ffffff",
    "palette":
    "#2e3436:#ff007a:#84ff39:#f3d56e:#7cb7ff:#c74ded:#00e8c6:#d3d7cf:#555753:#ff007a:#84ff39:#f3d56e:#7cb7ff:#c74ded:#00e8c6:#eeeeec",
    "type": "dark"
}, {
    "name": "Neopolitan",
    "palette":
    "#000000:#800000:#61ce3c:#fbde2d:#253b76:#ff0080:#8da6ce:#f8f8f8:#000000:#800000:#61ce3c:#fbde2d:#253b76:#ff0080:#8da6ce:#f8f8f8",
    "background_color": "#271f19",
    "cursor_color": "#ffffff",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Neutron",
    "palette":
    "#23252b:#b54036:#5ab977:#deb566:#6a7c93:#a4799d:#3f94a8:#e6e8ef:#23252b:#b54036:#5ab977:#deb566:#6a7c93:#a4799d:#3f94a8:#ebedf2",
    "background_color": "#1c1e22",
    "cursor_color": "#f6f7ec",
    "foreground_color": "#e6e8ef",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Night Owl",
    "background_color": "#011627",
    "cursor_color": "#80a4c2",
    "cursor_color_fg": "False",
    "foreground_color": "#d6deeb",
    "palette":
    "#2e3436:#ef5350:#80cbc4:#ffeb95:#82aaff:#c792ea:#addb67:#d3d7cf:#555753:#ef5350:#80cbc4:#ffeb95:#82aaff:#c792ea:#addb67:#eeeeec",
    "type": "dark"
}, {
    "name": "NightLion v1",
    "palette":
    "#4c4c4c:#bb0000:#5fde8f:#f3f167:#276bd8:#bb00bb:#00dadf:#bbbbbb:#555555:#ff5555:#55ff55:#ffff55:#5555ff:#ff55ff:#55ffff:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bbbbbb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "NightLion v2",
    "palette":
    "#4c4c4c:#bb0000:#04f623:#f3f167:#64d0f0:#ce6fdb:#00dadf:#bbbbbb:#555555:#ff5555:#7df71d:#ffff55:#62cbe8:#ff9bf5:#00ccd8:#ffffff",
    "background_color": "#171717",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bbbbbb",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Nord",
    "background_color": "#2E3440",
    "cursor_color": "#D8DEE9",
    "foreground_color": "#D8DEE9",
    "palette":
    "#3B4252:#BF616A:#A3BE8C:#EBCB8B:#81A1C1:#B48EAD:#88C0D0:#E5E9F0:#4C566A:#BF616A:#A3BE8C:#EBCB8B:#81A1C1:#B48EAD:#8FBCBB:#ECEFF4",
    "type": "dark"
}, {
    "name": "Novel",
    "palette":
    "#000000:#cc0000:#009600:#d06b00:#0000cc:#cc00cc:#0087cc:#cccccc:#808080:#cc0000:#009600:#d06b00:#0000cc:#cc00cc:#0087cc:#ffffff",
    "background_color": "#dfdbc3",
    "cursor_color": "#73635a",
    "foreground_color": "#3b2322",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Obsidian",
    "palette":
    "#000000:#a60001:#00bb00:#fecd22:#3a9bdb:#bb00bb:#00bbbb:#bbbbbb:#555555:#ff0003:#93c863:#fef874:#a1d7ff:#ff55ff:#55ffff:#ffffff",
    "background_color": "#283033",
    "cursor_color": "#c0cad0",
    "foreground_color": "#cdcdcd",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ocean",
    "palette":
    "#000000:#990000:#00a600:#999900:#0000b2:#b200b2:#00a6b2:#bfbfbf:#666666:#e50000:#00d900:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#224fbc",
    "cursor_color": "#7f7f7f",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ocean dark",
    "background_color": "#1c1f27",
    "background_image": "None",
    "cursor_color": "#a0a4b2",
    "foreground_color": "#979cac",
    "palette":
    "#4F4F4F:#AF4B57:#AFD383:#E5C079:#7D90A4:#A4799D:#85A6A5:#EEEDEE:#7B7B7B:#AF4B57:#CEFFAB:#FFFECC:#B5DCFE:#FB9BFE:#DFDFFD:#FEFFFE",
    "type": "dark"
}, {
    "name": "OceanicMaterial",
    "palette":
    "#000000:#ee2b2a:#40a33f:#ffea2e:#1e80f0:#8800a0:#16afca:#a4a4a4:#777777:#dc5c60:#70be71:#fff163:#54a4f3:#aa4dbc:#42c7da:#ffffff",
    "background_color": "#1c262b",
    "cursor_color": "#b3b8c3",
    "foreground_color": "#c2c8d7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ollie",
    "palette":
    "#000000:#ac2e31:#31ac61:#ac4300:#2d57ac:#b08528:#1fa6ac:#8a8eac:#5b3725:#ff3d48:#3bff99:#ff5e1e:#4488ff:#ffc21d:#1ffaff:#5b6ea7",
    "background_color": "#222125",
    "cursor_color": "#5b6ea7",
    "foreground_color": "#8a8dae",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "One dark",
    "background_color": "#1e2127",
    "background_image": "None",
    "cursor_color": "#676c76",
    "foreground_color": "#5c6370",
    "palette":
    "#000000:#e06c75:#98c379:#d19a66:#61afef:#c678dd:#56b6c2:#abb2bf:#5c6370:#e06c75:#98c379:#d19a66:#61afef:#c678dd:#56b6c2:#fffefe",
    "type": "dark"
}, {
    "name": "OneHalfDark",
    "palette":
    "#282c34:#e06c75:#98c379:#e5c07b:#61afef:#c678dd:#56b6c2:#dcdfe4:#282c34:#e06c75:#98c379:#e5c07b:#61afef:#c678dd:#56b6c2:#dcdfe4",
    "background_color": "#282c34",
    "cursor_color": "#a3b3cc",
    "foreground_color": "#dcdfe4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "OneHalfLight",
    "palette":
    "#383a42:#e45649:#50a14f:#c18401:#0184bc:#a626a4:#0997b3:#fafafa:#4f525e:#e06c75:#98c379:#e5c07b:#61afef:#c678dd:#56b6c2:#ffffff",
    "background_color": "#fafafa",
    "cursor_color": "#bfceff",
    "foreground_color": "#383a42",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Pali",
    "background_color": "#232e37",
    "background_image": "None",
    "cursor_color": "#e3ecf5",
    "foreground_color": "#d9e6f2",
    "palette":
    "#0a0a0a:#ab8f74:#74ab8f:#8fab74:#8f74ab:#ab748f:#748fab:#f2f2f2:#5d5d5d:#ff1d62:#9cc3af:#ffd00a:#af9cc3:#ff1d62:#4bb8fd:#a020f0",
    "type": "dark"
}, {
    "name": "Panda",
    "background_color": "#292a2b",
    "cursor_color": "#f0eeee",
    "foreground_color": "#e6e6e6",
    "palette":
    "#676b79:#ff2c6d:#19f9d8:#ffb86c:#45a9f9:#b084eb:#6fc1ff:#d3d7cf:#676b79:#ff9ac1:#19f9d8:#ffcc95:#45a9f9:#b084eb:#6fc1ff:#eeeeec",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Pandora",
    "palette":
    "#000000:#ff4242:#74af68:#ffad29:#338f86:#9414e6:#23d7d7:#e2e2e2:#3f5648:#ff3242:#74cd68:#ffb929:#23d7d7:#ff37ff:#00ede1:#ffffff",
    "background_color": "#141e43",
    "cursor_color": "#43d58e",
    "foreground_color": "#e1e1e1",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Paraiso Dark",
    "palette":
    "#2f1e2e:#ef6155:#48b685:#fec418:#06b6ef:#815ba4:#5bc4bf:#a39e9b:#776e71:#ef6155:#48b685:#fec418:#06b6ef:#815ba4:#5bc4bf:#e7e9db",
    "background_color": "#2f1e2e",
    "cursor_color": "#a39e9b",
    "foreground_color": "#a39e9b",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Parasio Dark",
    "palette":
    "#2f1e2e:#ef6155:#48b685:#fec418:#06b6ef:#815ba4:#5bc4bf:#a39e9b:#776e71:#ef6155:#48b685:#fec418:#06b6ef:#815ba4:#5bc4bf:#e7e9db",
    "background_color": "#2f1e2e",
    "cursor_color": "#a39e9b",
    "foreground_color": "#a39e9b",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "PaulMillr",
    "palette":
    "#2a2a2a:#ff0000:#79ff0f:#e7bf00:#396bd7:#b449be:#66ccff:#bbbbbb:#666666:#ff0080:#66ff66:#f3d64e:#709aed:#db67e6:#7adff2:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#4d4d4d",
    "foreground_color": "#f2f2f2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "PencilDark",
    "palette":
    "#212121:#c30771:#10a778:#a89c14:#008ec4:#523c79:#20a5ba:#d9d9d9:#424242:#fb007a:#5fd7af:#f3e430:#20bbfc:#6855de:#4fb8cc:#f1f1f1",
    "background_color": "#212121",
    "cursor_color": "#20bbfc",
    "foreground_color": "#f1f1f1",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "PencilLight",
    "palette":
    "#212121:#c30771:#10a778:#a89c14:#008ec4:#523c79:#20a5ba:#d9d9d9:#424242:#fb007a:#5fd7af:#f3e430:#20bbfc:#6855de:#4fb8cc:#f1f1f1",
    "background_color": "#f1f1f1",
    "cursor_color": "#20bbfc",
    "foreground_color": "#424242",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Peppermint",
    "background_image": "None",
    "cursor_color": "#BBBBBB",
    "foreground_color": "#c7c7c7",
    "palette":
    "#353535:#E64569:#89D287:#DAB752:#439ECF:#D961DC:#64AAAF:#B3B3B3:#535353:#E4859A:#A2CCA1:#E1E387:#6FBBE2:#E586E7:#96DCDA:#DEDEDE",
    "type": "dark"
}, {
    "name": "Piatto Light",
    "palette":
    "#414141:#b23771:#66781e:#cd6f34:#3c5ea8:#a454b2:#66781e:#ffffff:#3f3f3f:#db3365:#829429:#cd6f34:#3c5ea8:#a454b2:#829429:#f2f2f2",
    "background_color": "#ffffff",
    "cursor_color": "#5e77c8",
    "foreground_color": "#414141",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Pnevma",
    "palette":
    "#2f2e2d:#a36666:#90a57d:#d7af87:#7fa5bd:#c79ec4:#8adbb4:#d0d0d0:#4a4845:#d78787:#afbea2:#e4c9af:#a1bdce:#d7beda:#b1e7dd:#efefef",
    "background_color": "#1c1c1c",
    "cursor_color": "#e4c9af",
    "foreground_color": "#d0d0d0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Pro",
    "palette":
    "#000000:#990000:#00a600:#999900:#2009db:#b200b2:#00a6b2:#bfbfbf:#666666:#e50000:#00d900:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#000000",
    "cursor_color": "#4d4d4d",
    "foreground_color": "#f2f2f2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Red Alert",
    "palette":
    "#000000:#d62e4e:#71be6b:#beb86b:#489bee:#e979d7:#6bbeb8:#d6d6d6:#262626:#e02553:#aff08c:#dfddb7:#65aaf1:#ddb7df:#b7dfdd:#ffffff",
    "background_color": "#762423",
    "cursor_color": "#ffffff",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Red Planet",
    "palette":
    "#202020:#8c3432:#728271:#e8bf6a:#69819e:#896492:#5b8390:#b9aa99:#676767:#b55242:#869985:#ebeb91:#60827e:#de4974:#38add8:#d6bfb8",
    "background_color": "#222222",
    "cursor_color": "#c2b790",
    "foreground_color": "#c2b790",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Red Sands",
    "palette":
    "#000000:#ff3f00:#00bb00:#e7b000:#0072ff:#bb00bb:#00bbbb:#bbbbbb:#555555:#bb0000:#00bb00:#e7b000:#0072ae:#ff55ff:#55ffff:#ffffff",
    "background_color": "#7a251e",
    "cursor_color": "#ffffff",
    "foreground_color": "#d7c9a7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Relaxed",
    "palette":
    "#151515:#bc5653:#909d63:#ebc17a:#6a8799:#b06698:#c9dfff:#d9d9d9:#636363:#bc5653:#a0ac77:#ebc17a:#7eaac7:#b06698:#acbbd0:#f7f7f7",
    "background_color": "#353a44",
    "cursor_color": "#d9d9d9",
    "foreground_color": "#d9d9d9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Rippedcasts",
    "palette":
    "#000000:#cdaf95:#a8ff60:#bfbb1f:#75a5b0:#ff73fd:#5a647e:#bfbfbf:#666666:#eecbad:#bcee68:#e5e500:#86bdc9:#e500e5:#8c9bc4:#e5e5e5",
    "background_color": "#2b2b2b",
    "cursor_color": "#7f7f7f",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Rose Pine",
    "background_color": "#191724",
    "cursor_color": "#9ccfd8",
    "foreground_color": "#e0def4",
    "palette":
    "#26233A:#eb6f91:#9ccfd8:#f6c177:#31748f:#65618d:#c4a7e7:#d3d7cf:#26233a:#eb6f91:#9ccfd8:#f6c177:#31748f:#65618d:#c4a7e7:#eeeeec",
    "type": "dark"
}, {
    "name": "Royal",
    "palette":
    "#241f2b:#91284c:#23801c:#b49d27:#6580b0:#674d96:#8aaabe:#524966:#312d3d:#d5356c:#2cd946:#fde83b:#90baf9:#a479e3:#acd4eb:#9e8cbd",
    "background_color": "#100815",
    "cursor_color": "#524966",
    "foreground_color": "#514968",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ryuuko",
    "palette":
    "#2c3941:#865f5b:#66907d:#b1a990:#6a8e95:#b18a73:#88b2ac:#ececec:#5d7079:#865f5b:#66907d:#b1a990:#6a8e95:#b18a73:#88b2ac:#ececec",
    "background_color": "#2c3941",
    "cursor_color": "#ececec",
    "foreground_color": "#ececec",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Seafoam Pastel",
    "palette":
    "#757575:#825d4d:#728c62:#ada16d:#4d7b82:#8a7267:#729494:#e0e0e0:#8a8a8a:#cf937a:#98d9aa:#fae79d:#7ac3cf:#d6b2a1:#ade0e0:#e0e0e0",
    "background_color": "#243435",
    "cursor_color": "#57647a",
    "foreground_color": "#d4e7d4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "SeaShells",
    "palette":
    "#17384c:#d15123:#027c9b:#fca02f:#1e4950:#68d4f1:#50a3b5:#deb88d:#434b53:#d48678:#628d98:#fdd39f:#1bbcdd:#bbe3ee:#87acb4:#fee4ce",
    "background_color": "#09141b",
    "cursor_color": "#fca02f",
    "foreground_color": "#deb88d",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Seti",
    "palette":
    "#323232:#c22832:#8ec43d:#e0c64f:#43a5d5:#8b57b5:#8ec43d:#eeeeee:#323232:#c22832:#8ec43d:#e0c64f:#43a5d5:#8b57b5:#8ec43d:#ffffff",
    "background_color": "#111213",
    "cursor_color": "#e3bf21",
    "foreground_color": "#cacecd",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Shaman",
    "palette":
    "#012026:#b2302d:#00a941:#5e8baa:#449a86:#00599d:#5d7e19:#405555:#384451:#ff4242:#2aea5e:#8ed4fd:#61d5ba:#1298ff:#98d028:#58fbd6",
    "background_color": "#001015",
    "cursor_color": "#4afcd6",
    "foreground_color": "#405555",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Shel",
    "background_color": "#2a201f",
    "background_image": "None",
    "cursor_color": "#6192d2",
    "foreground_color": "#4882cd",
    "palette":
    "#2c2423:#ab2463:#6ca323:#ab6423:#2c64a2:#6c24a2:#2ca363:#918988:#918988:#f588b9:#c2ee86:#f5ba86:#8fbaec:#c288ec:#8feeb9:#f5eeec",
    "type": "dark"
}, {
    "name": "Sick",
    "background_color": "#272935",
    "cursor_color": "#aaaaaa",
    "foreground_color": "#aeaeb1",
    "palette":
    "#2e3436:#f47375:#6bf1be:#e5f081:#6aa1fd:#c481ff:#6de4fd:#d3d7cf:#555753:#f47375:#6bf1be:#e5f081:#6aa1fd:#c481ff:#6de4fd:#eeeeec",
    "type": "dark"
}, {
    "name": "Slate",
    "palette":
    "#222222:#e2a8bf:#81d778:#c4c9c0:#264b49:#a481d3:#15ab9c:#02c5e0:#ffffff:#ffcdd9:#beffa8:#d0ccca:#7ab0d2:#c5a7d9:#8cdfe0:#e0e0e0",
    "background_color": "#222222",
    "cursor_color": "#87d3c4",
    "foreground_color": "#35b1d2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Smyck",
    "palette":
    "#000000:#b84131:#7da900:#c4a500:#62a3c4:#ba8acc:#207383:#a1a1a1:#7a7a7a:#d6837c:#c4f137:#fee14d:#8dcff0:#f79aff:#6ad9cf:#f7f7f7",
    "background_color": "#1b1b1b",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#f7f7f7",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Snazzy",
    "background_color": "#242424",
    "background_image": "None",
    "cursor_color": "#97979b",
    "foreground_color": "#eff0eb",
    "palette":
    "#282a36:#ff5c57:#5af78e:#f3f99d:#57c7ff:#ff6ac1:#9aedfe:#f1f1f0:#686868:#ff5c57:#5af78e:#f3f99d:#57c7ff:#ff6ac1:#9aedfe:#eff0eb",
    "type": "dark"
}, {
    "name": "SoftServer",
    "palette":
    "#000000:#a2686a:#9aa56a:#a3906a:#6b8fa3:#6a71a3:#6ba58f:#99a3a2:#666c6c:#dd5c60:#bfdf55:#deb360:#62b1df:#606edf:#64e39c:#d2e0de",
    "background_color": "#242626",
    "cursor_color": "#d2e0de",
    "foreground_color": "#99a3a2",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Solarized Darcula",
    "palette":
    "#25292a:#f24840:#629655:#b68800:#2075c7:#797fd4:#15968d:#d2d8d9:#25292a:#f24840:#629655:#b68800:#2075c7:#797fd4:#15968d:#d2d8d9",
    "background_color": "#3d3f41",
    "cursor_color": "#708284",
    "foreground_color": "#d2d8d9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Solarized Dark",
    "palette":
    "#073642:#dc322f:#859900:#b58900:#268bd2:#d33682:#2aa198:#eee8d5:#586e75:#cb4b16:#586e75:#657b83:#839496:#6c71c4:#93a1a1:#fdf6e3",
    "foreground_color": "#eee8d5",
    "background_color": "#002b36",
    "cursor_color": "#eee8d5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Solarized Dark - Patched",
    "palette":
    "#002831:#d11c24:#738a05:#a57706:#2176c7:#c61c6f:#259286:#eae3cb:#475b62:#bd3613:#475b62:#536870:#708284:#5956ba:#819090:#fcf4dc",
    "background_color": "#001e27",
    "cursor_color": "#708284",
    "foreground_color": "#708284",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Solarized Dark Higher Contrast",
    "palette":
    "#002831:#d11c24:#6cbe6c:#a57706:#2176c7:#c61c6f:#259286:#eae3cb:#006488:#f5163b:#51ef84:#b27e28:#178ec8:#e24d8e:#00b39e:#fcf4dc",
    "background_color": "#001e27",
    "cursor_color": "#f34b00",
    "foreground_color": "#9cc2c3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Solarized Light",
    "palette":
    "#073642:#dc322f:#859900:#b58900:#268bd2:#d33682:#2aa198:#eee8d5:#002b36:#cb4b16:#586e75:#657b83:#839496:#6c71c4:#93a1a1:#fdf6e3",
    "background_color": "#eee8d5",
    "foreground_color": "#002b36",
    "cursor_color": "#002b36",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Spacedust",
    "palette":
    "#6e5346:#e35b00:#5cab96:#e3cd7b:#0f548b:#e35b00:#06afc7:#f0f1ce:#684c31:#ff8a3a:#aecab8:#ffc878:#67a0ce:#ff8a3a:#83a7b4:#fefff1",
    "background_color": "#0a1e24",
    "cursor_color": "#708284",
    "foreground_color": "#ecf0c1",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "SpaceGray",
    "palette":
    "#000000:#b04b57:#87b379:#e5c179:#7d8fa4:#a47996:#85a7a5:#b3b8c3:#000000:#b04b57:#87b379:#e5c179:#7d8fa4:#a47996:#85a7a5:#ffffff",
    "background_color": "#20242d",
    "cursor_color": "#b3b8c3",
    "foreground_color": "#b3b8c3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "SpaceGray Eighties",
    "palette":
    "#15171c:#ec5f67:#81a764:#fec254:#5486c0:#bf83c1:#57c2c1:#efece7:#555555:#ff6973:#93d493:#ffd256:#4d84d1:#ff55ff:#83e9e4:#ffffff",
    "background_color": "#222222",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#bdbaae",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "SpaceGray Eighties Dull",
    "palette":
    "#15171c:#b24a56:#92b477:#c6735a:#7c8fa5:#a5789e:#80cdcb:#b3b8c3:#555555:#ec5f67:#89e986:#fec254:#5486c0:#bf83c1:#58c2c1:#ffffff",
    "background_color": "#222222",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#c9c6bc",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Spiderman",
    "palette":
    "#1b1d1e:#e60813:#e22928:#e24756:#2c3fff:#2435db:#3256ff:#fffef6:#505354:#ff0325:#ff3338:#fe3a35:#1d50ff:#747cff:#6184ff:#fffff9",
    "background_color": "#1b1d1e",
    "cursor_color": "#2c3fff",
    "foreground_color": "#e3e3e3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Spring",
    "palette":
    "#000000:#ff4d83:#1f8c3b:#1fc95b:#1dd3ee:#8959a8:#3e999f:#ffffff:#000000:#ff0021:#1fc231:#d5b807:#15a9fd:#8959a8:#3e999f:#ffffff",
    "background_color": "#ffffff",
    "cursor_color": "#4d4d4c",
    "foreground_color": "#4d4d4c",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Square",
    "palette":
    "#050505:#e9897c:#b6377d:#ecebbe:#a9cdeb:#75507b:#c9caec:#f2f2f2:#141414:#f99286:#c3f786:#fcfbcc:#b6defb:#ad7fa8:#d7d9fc:#e2e2e2",
    "background_color": "#1a1a1a",
    "cursor_color": "#fcfbcc",
    "foreground_color": "#acacab",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Sundried",
    "palette":
    "#302b2a:#a7463d:#587744:#9d602a:#485b98:#864651:#9c814f:#c9c9c9:#4d4e48:#aa000c:#128c21:#fc6a21:#7999f7:#fd8aa1:#fad484:#ffffff",
    "background_color": "#1a1818",
    "cursor_color": "#ffffff",
    "foreground_color": "#c9c9c9",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Symfonic",
    "palette":
    "#000000:#dc322f:#56db3a:#ff8400:#0084d4:#b729d9:#ccccff:#ffffff:#1b1d21:#dc322f:#56db3a:#ff8400:#0084d4:#b729d9:#ccccff:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#dc322f",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Teerb",
    "palette":
    "#1c1c1c:#d68686:#aed686:#d7af87:#86aed6:#d6aed6:#8adbb4:#d0d0d0:#1c1c1c:#d68686:#aed686:#e4c9af:#86aed6:#d6aed6:#b1e7dd:#efefef",
    "background_color": "#262626",
    "cursor_color": "#e4c9af",
    "foreground_color": "#d0d0d0",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Terminal Basic",
    "palette":
    "#000000:#990000:#00a600:#999900:#0000b2:#b200b2:#00a6b2:#bfbfbf:#666666:#e50000:#00d900:#e5e500:#0000ff:#e500e5:#00e5e5:#e5e5e5",
    "background_color": "#ffffff",
    "cursor_color": "#7f7f7f",
    "foreground_color": "#000000",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Thayer Bright",
    "palette":
    "#1b1d1e:#f92672:#4df840:#f4fd22:#2757d6:#8c54fe:#38c8b5:#ccccc6:#505354:#ff5995:#b6e354:#feed6c:#3f78ff:#9e6ffe:#23cfd5:#f8f8f2",
    "background_color": "#1b1d1e",
    "cursor_color": "#fc971f",
    "foreground_color": "#f8f8f8",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "The Hulk",
    "palette":
    "#1b1d1e:#269d1b:#13ce30:#63e457:#2525f5:#641f74:#378ca9:#d9d8d1:#505354:#8dff2a:#48ff77:#3afe16:#506b95:#72589d:#4085a6:#e5e6e1",
    "background_color": "#1b1d1e",
    "cursor_color": "#16b61b",
    "foreground_color": "#b5b5b5",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Tomorrow",
    "palette":
    "#000000:#c82829:#718c00:#eab700:#4271ae:#8959a8:#3e999f:#ffffff:#000000:#c82829:#718c00:#eab700:#4271ae:#8959a8:#3e999f:#ffffff",
    "background_color": "#ffffff",
    "cursor_color": "#4d4d4c",
    "foreground_color": "#4d4d4c",
    "background_image": "None",
    "type": "light"
}, {
    "name": "Tomorrow Night",
    "palette":
    "#000000:#cc6666:#b5bd68:#f0c674:#81a2be:#b294bb:#8abeb7:#ffffff:#000000:#cc6666:#b5bd68:#f0c674:#81a2be:#b294bb:#8abeb7:#ffffff",
    "background_color": "#1d1f21",
    "cursor_color": "#c5c8c6",
    "foreground_color": "#c5c8c6",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Tomorrow Night Blue",
    "palette":
    "#000000:#ff9da4:#d1f1a9:#ffeead:#bbdaff:#ebbbff:#99ffff:#ffffff:#000000:#ff9da4:#d1f1a9:#ffeead:#bbdaff:#ebbbff:#99ffff:#ffffff",
    "background_color": "#002451",
    "cursor_color": "#ffffff",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Tomorrow Night Bright",
    "palette":
    "#000000:#d54e53:#b9ca4a:#e7c547:#7aa6da:#c397d8:#70c0b1:#ffffff:#000000:#d54e53:#b9ca4a:#e7c547:#7aa6da:#c397d8:#70c0b1:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#eaeaea",
    "foreground_color": "#eaeaea",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Tomorrow Night Eighties",
    "palette":
    "#000000:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#ffffff:#000000:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#ffffff",
    "background_color": "#2d2d2d",
    "cursor_color": "#cccccc",
    "foreground_color": "#cccccc",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "ToyChest",
    "palette":
    "#2c3f58:#be2d26:#1a9172:#db8e27:#325d96:#8a5edc:#35a08f:#23d183:#336889:#dd5944:#31d07b:#e7d84b:#34a6da:#ae6bdc:#42c3ae:#d5d5d5",
    "background_color": "#24364b",
    "cursor_color": "#d5d5d5",
    "foreground_color": "#31d07b",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Treehouse",
    "palette":
    "#321300:#b2270e:#44a900:#aa820c:#58859a:#97363d:#b25a1e:#786b53:#433626:#ed5d20:#55f238:#f2b732:#85cfed:#e14c5a:#f07d14:#ffc800",
    "background_color": "#191919",
    "cursor_color": "#fac814",
    "foreground_color": "#786b53",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Twilight",
    "palette":
    "#141414:#c06d44:#afb97a:#c2a86c:#44474a:#b4be7c:#778385:#ffffd4:#262626:#de7c4c:#ccd88c:#e2c47e:#5a5e62:#d0dc8e:#8a989b:#ffffd4",
    "background_color": "#141414",
    "cursor_color": "#ffffff",
    "foreground_color": "#ffffd4",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Ubuntu",
    "palette":
    "#2e3436:#cc0000:#4e9a06:#c4a000:#3465a4:#75507b:#06989a:#d3d7cf:#555753:#ef2929:#8ae234:#fce94f:#729fcf:#ad7fa8:#34e2e2:#eeeeec",
    "background_color": "#300a24",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#eeeeec",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "UnderTheSea",
    "palette":
    "#022026:#b2302d:#00a941:#59819c:#459a86:#00599d:#5d7e19:#405555:#384451:#ff4242:#2aea5e:#8ed4fd:#61d5ba:#1298ff:#98d028:#58fbd6",
    "background_color": "#011116",
    "cursor_color": "#4afcd6",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Urple",
    "palette":
    "#000000:#b0425b:#37a415:#ad5c42:#564d9b:#6c3ca1:#808080:#87799c:#5d3225:#ff6388:#29e620:#f08161:#867aed:#a05eee:#eaeaea:#bfa3ff",
    "background_color": "#1b1b23",
    "cursor_color": "#a063eb",
    "foreground_color": "#877a9b",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Vag",
    "background_color": "#191f1d",
    "background_image": "None",
    "cursor_color": "#e5f0fa",
    "foreground_color": "#d9e6f2",
    "palette":
    "#303030:#a87139:#39a871:#71a839:#7139a8:#a83971:#3971a8:#8a8a8a:#494949:#b0763b:#3bb076:#76b03b:#763bb0:#b03b76:#3b76b0:#cfcfcf",
    "type": "dark"
}, {
    "name": "Vaughn",
    "palette":
    "#25234f:#705050:#60b48a:#dfaf8f:#5555ff:#f08cc3:#8cd0d3:#709080:#709080:#dca3a3:#60b48a:#f0dfaf:#5555ff:#ec93d3:#93e0e3:#ffffff",
    "background_color": "#25234f",
    "cursor_color": "#ff5555",
    "foreground_color": "#dcdccc",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Venom",
    "background_color": "#060d14",
    "cursor_color": "#9ecfa2",
    "foreground_color": "#668198",
    "palette":
    "#2e3436:#e94759:#9ecfa2:#f3efa9:#00898d:#9c21b0:#06989a:#d3d7cf:#555753:#ef2929:#8ae234:#fce94f:#729fcf:#ad7fa8:#34e2e2:#eeeeec",
    "type": "dark"
}, {
    "name": "VibrantInk",
    "palette":
    "#878787:#ff6600:#ccff04:#ffcc00:#44b4cc:#9933cc:#44b4cc:#f5f5f5:#555555:#ff0000:#00ff00:#ffff00:#0000ff:#ff00ff:#00ffff:#e5e5e5",
    "background_color": "#000000",
    "cursor_color": "#ffffff",
    "foreground_color": "#ffffff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Violet Dark",
    "palette":
    "#56595c:#c94c22:#85981c:#b4881d:#2e8bce:#d13a82:#32a198:#c9c6bd:#45484b:#bd3613:#738a04:#a57705:#2176c7:#c61c6f:#259286:#c9c6bd",
    "background_color": "#1c1d1f",
    "cursor_color": "#708284",
    "foreground_color": "#708284",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Violet Light",
    "palette":
    "#56595c:#c94c22:#85981c:#b4881d:#2e8bce:#d13a82:#32a198:#d3d0c9:#45484b:#bd3613:#738a04:#a57705:#2176c7:#c61c6f:#259286:#c9c6bd",
    "background_color": "#fcf4dc",
    "cursor_color": "#536870",
    "foreground_color": "#536870",
    "background_image": "None",
    "type": "light"
}, {
    "name": "WarmNeon",
    "palette":
    "#000000:#e24346:#39b13a:#dae145:#4261c5:#f920fb:#2abbd4:#d0b8a3:#fefcfc:#e97071:#9cc090:#ddda7a:#7b91d6:#f674ba:#5ed1e5:#d8c8bb",
    "background_color": "#404040",
    "cursor_color": "#30ff24",
    "foreground_color": "#afdab6",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Wez",
    "palette":
    "#000000:#cc5555:#55cc55:#cdcd55:#5555cc:#cc55cc:#7acaca:#cccccc:#555555:#ff5555:#55ff55:#ffff55:#5555ff:#ff55ff:#55ffff:#ffffff",
    "background_color": "#000000",
    "cursor_color": "#53ae71",
    "foreground_color": "#b3b3b3",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "WildCherry",
    "palette":
    "#000507:#d94085:#2ab250:#ffd16f:#883cdc:#ececec:#c1b8b7:#fff8de:#009cc9:#da6bac:#f4dca5:#eac066:#308cba:#ae636b:#ff919d:#e4838d",
    "background_color": "#1f1726",
    "cursor_color": "#dd00ff",
    "foreground_color": "#dafaff",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Wombat",
    "palette":
    "#000000:#ff615a:#b1e969:#ebd99c:#5da9f6:#e86aff:#82fff7:#dedacf:#313131:#f58c80:#ddf88f:#eee5b2:#a5c7ff:#ddaaff:#b7fff9:#ffffff",
    "background_color": "#171717",
    "cursor_color": "#bbbbbb",
    "foreground_color": "#dedacf",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Wryan",
    "palette":
    "#333333:#8c4665:#287373:#7c7c99:#395573:#5e468c:#31658c:#899ca1:#3d3d3d:#bf4d80:#53a6a6:#9e9ecb:#477ab3:#7e62b3:#6096bf:#c0c0c0",
    "background_color": "#101010",
    "cursor_color": "#9e9ecb",
    "foreground_color": "#999993",
    "background_image": "None",
    "type": "dark"
}, {
    "name": "Zenburn",
    "palette":
    "#4d4d4d:#705050:#60b48a:#f0dfaf:#506070:#dc8cc3:#8cd0d3:#dcdccc:#709080:#dca3a3:#c3bf9f:#e0cf9f:#94bff3:#ec93d3:#93e0e3:#ffffff",
    "background_color": "#3f3f3f",
    "cursor_color": "#73635a",
    "foreground_color": "#dcdccc",
    "background_image": "None",
    "type": "dark"
}]


class TerminatorThemes(plugin.Plugin):

    capabilities = ['terminal_menu']
    config_base = ConfigBase()
    # base_url = 'https://api.github.com/repos/EliverLara/terminator-themes/contents/themes.json'
    base_url = 'https://gitee.com/winnochan/terminator-themes/raw/master/themes.json'
    inherits_config_from = "default"

    def callback(self, menuitems, menu, terminal):
        """Add our item to the menu"""
        self.terminal = terminal
        item = Gtk.ImageMenuItem(Gtk.STOCK_FIND)
        item.connect('activate', self.configure)
        item.set_label("Themes")
        item.set_sensitive(True)
        menuitems.append(item)

    def configure(self, widget, data=None):
        ui = {}
        dbox = Gtk.Dialog(_("Terminator themes"), None, Gtk.DialogFlags.MODAL)

        # headers = { "Accept": "application/vnd.github.v3.raw" }
        # response = requests.get(self.base_url, headers=headers)
        # response = requests.get(self.base_url)

        # if response.status_code != 200:
        #     gerr(_("Failed to get list of available themes"))
        #     return

        # self.themes_from_repo = response.json()["themes"]
        self.themes_from_repo = themes
        self.profiles = self.terminal.config.list_profiles()

        main_container = Gtk.HBox(spacing=5)
        main_container.pack_start(self._create_themes_grid(ui), True, True,
                                  0)  #Left column
        main_container.pack_start(self._create_settings_grid(ui), True, True,
                                  0)  #Right column

        dbox.vbox.pack_start(main_container, True, True, 0)

        self.dbox = dbox
        dbox.show_all()
        res = dbox.run()

        if res == Gtk.ResponseType.ACCEPT:
            self.terminal.config.save()

        del (self.dbox)
        dbox.destroy()

        return

    def _create_themes_grid(self, ui):
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(7)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)

        scroll_window = self._create_themes_list(ui)

        (combo, search_entry) = self._create_filter_widgets(ui)

        grid.attach(search_entry, 0, 0, 2, 1)
        grid.attach(combo, 2, 0, 1, 1)
        grid.attach(scroll_window, 0, 1, 3, 10)

        return grid

    def _create_filter_widgets(self, ui):

        combo = Gtk.ComboBoxText()
        combo.set_entry_text_column(0)
        combo.connect("changed", self.on_filter_combo_changed)
        combo.append_text("Filter by type")

        for theme_type in ["light", "dark", "All"]:
            combo.append_text(theme_type)

        combo.set_active(0)

        search_entry = Gtk.SearchEntry(max_width_chars=30)
        search_entry.connect("search-changed", self.on_theme_search_changed,
                             ui)

        return [combo, search_entry]

    def _create_themes_list(self, ui):

        profiles_list_model = Gtk.ListStore(str, str, bool, object)
        # Set add/remove buttons availability
        for theme in self.themes_from_repo:
            if theme["name"] in self.profiles:
                profiles_list_model.append(
                    [theme["name"], theme["type"], False, theme])
            else:
                profiles_list_model.append(
                    [theme["name"], theme["type"], True, theme])

        self.current_filter_theme = None
        self.filter_type = "theme_type"
        self.theme_filter = profiles_list_model.filter_new()
        self.theme_filter.set_visible_func(self.theme_filter_func)

        treeview = Gtk.TreeView.new_with_model(self.theme_filter)

        selection = treeview.get_selection()
        selection.set_mode(Gtk.SelectionMode.SINGLE)
        selection.connect("changed", self.on_selection_changed, ui)
        ui['treeview'] = treeview

        for i, column_title in enumerate(["Theme", "Type"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            treeview.append_column(column)

        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC,
                                 Gtk.PolicyType.AUTOMATIC)
        scroll_window.add(treeview)

        return scroll_window

    def _create_settings_grid(self, ui):
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(7)
        grid.attach(self._create_default_inherits_check(ui), 0, 15, 2, 1)
        grid.attach(Gtk.Label("Available profiles: "), 0, 16, 1, 1)
        grid.attach(self._create_inherits_from_combo(ui), 1, 16, 1, 1)
        grid.attach(
            self._create_main_action_button(ui, "install", self.on_install), 0,
            20, 1, 1)
        grid.attach(
            self._create_main_action_button(ui, "remove", self.on_uninstall),
            1, 20, 1, 1)
        self.theme_preview = ThemePreview(self.themes_from_repo[0])
        grid.attach(self.theme_preview, 0, 10, 4, 2)

        return grid

    def _create_default_inherits_check(self, ui):
        check = Gtk.CheckButton("Inherit preferences from default profile")
        check.set_active(True)
        check.connect("toggled", self.on_inheritsfromdefaultcheck_toggled, ui)
        ui['check_inherits_from_default'] = check

        return check

    def _create_inherits_from_combo(self, ui):
        combo = Gtk.ComboBoxText()
        combo.set_entry_text_column(0)
        combo.set_sensitive(False)
        combo.connect("changed", self.on_inheritsfromcombo_changed, ui)
        ui['inherits_from_combo'] = combo

        for profile in self.profiles:
            combo.append_text(profile)

        combo.set_active(
            self.profiles.index(self.terminal.config.get_profile())
        )  #set current terminal profile as current item

        return combo

    def _create_main_action_button(self, ui, label, action):
        btn = Gtk.Button(_(label.capitalize()))
        btn.connect("clicked", action, ui)
        btn.set_sensitive(False)
        ui['button_' + label] = btn

        return btn

    def theme_filter_func(self, model, iter, data):
        if self.filter_type == "theme_type":
            return self.filter_by_theme_type(model, iter, data)
        else:
            return self.filter_by_theme_search(model, iter, data)

    def filter_by_theme_search(self, model, iter, data):
        return model[iter][0].lower().find(self.current_filter_theme) > -1

    def filter_by_theme_type(self, model, iter, data):
        if self.current_filter_theme is None or self.current_filter_theme == "All":
            return True
        else:
            return model[iter][1] == self.current_filter_theme

    def on_theme_search_changed(self, widget, ui):
        self.filter_type = "theme_search"
        self.current_filter_theme = widget.get_text()
        self.theme_filter.refilter()

    def on_filter_combo_changed(self, widget):

        if widget.get_active() == 0:
            self.current_filter_theme = None
        else:
            self.current_filter_theme = widget.get_active_text()

        self.filter_type = "theme_type"

        # #we update the filter, which updates in turn the view
        self.theme_filter.refilter()

    def on_inheritsfromdefaultcheck_toggled(self, check, data=None):
        if check.get_active() is not True:
            data["inherits_from_combo"].set_sensitive(True)
            self.inherits_config_from = self.profiles[
                data['inherits_from_combo'].get_active()]
        else:
            data["inherits_from_combo"].set_sensitive(False)
            self.inherits_config_from = 'default'

    def on_inheritsfromcombo_changed(self, combo, data):
        if combo.get_sensitive():
            self.inherits_config_from = self.profiles[combo.get_active()]
        else:
            self.inherits_config_from = 'default'

    def on_selection_changed(self, selection, data=None):
        (model, iter) = selection.get_selected()
        data['button_install'].set_sensitive(model[iter][2])
        data['button_remove'].set_sensitive(model[iter][2] is not True)
        self.theme_preview.update_preview(model[iter][3])

    def on_uninstall(self, button, data):
        treeview = data['treeview']
        selection = treeview.get_selection()
        (store, iter) = selection.get_selected()
        target = store[iter][0]

        # If selected theme is active, sets terminal profile to default before unistalling
        if self.terminal.get_profile() == target:
            widget = self.terminal.get_vte()
            self.terminal.force_set_profile(widget, 'default')

        self.terminal.config.del_profile(target)
        self.terminal.config.save()
        self.update_comboInheritsFrom(data)

        #'Add' button available again
        data['treeview'].get_model().set_value(iter, 2, True)
        self.on_selection_changed(selection, data)

    def on_install(self, button, data):
        treeview = data['treeview']
        selection = treeview.get_selection()
        (store, iter) = selection.get_selected()
        target = store[iter][3]
        widget = self.terminal.get_vte()
        treeview.set_enable_tree_lines(False)

        if not iter:
            return

        self.terminal.config.add_profile(target["name"])
        template_data = self.config_base.profiles[
            self.inherits_config_from].copy()

        for k, v in target.items():
            if k != 'background_image' and k != 'name' and k != 'type':
                if k == 'background_darkness':
                    template_data[k] = float(v)
                else:
                    template_data[k] = v

        for k, v in template_data.items():
            self.config_base.set_item(k, v, target["name"])

        self.terminal.force_set_profile(widget, target["name"])
        self.terminal.config.save()
        self.update_comboInheritsFrom(data)

        # "Remove" button available again
        data['treeview'].get_model().set_value(iter, 2, False)
        self.on_selection_changed(selection, data)
        treeview.set_enable_tree_lines(True)

    def update_comboInheritsFrom(self, data):
        data['inherits_from_combo'].remove_all()
        profiles = self.terminal.config.list_profiles()
        self.profiles = profiles
        for profile in profiles:
            data['inherits_from_combo'].append_text(profile)

        data['inherits_from_combo'].set_active(
            profiles.index(self.terminal.config.get_profile()))


class ThemePreview(Gtk.VBox):
    def __init__(self, theme):
        Gtk.VBox.__init__(self)

        self.theme = theme
        self.palette_preview_colors = list()
        self.prompt_line = {}

        self.pack_start(self._create_preview_margin(), True, True, 0)
        self.pack_start(self._create_palette_preview(), False, False, 0)
        self.pack_start(self._create_preview_margin(), True, True, 0)
        self.pack_start(self._create_prompt_line(), True, True, 0)

        self.update_preview(self.theme)

    def _create_palette_preview(self):
        palette_preview = Gtk.FlowBox()
        palette_preview.set_min_children_per_line(10)
        palette_preview.set_max_children_per_line(10)
        palette_preview.set_selection_mode(Gtk.SelectionMode.NONE)

        palette_preview.add(Gtk.VBox())

        for color in self.theme['palette'].split(":")[0:8]:
            area = Gtk.DrawingArea()
            area.set_size_request(20, 25)
            color_preview = Gtk.VBox()
            color_preview.pack_start(area, False, False, 0)
            color_preview.modify_bg(0, color=Gdk.color_parse(color))

            self.palette_preview_colors.append(color_preview)

            palette_preview.add(color_preview)

        palette_preview.add(Gtk.VBox())

        return palette_preview

    def _create_prompt_line(self):
        line = Gtk.HBox()

        self.prompt_line["prompt"] = Gtk.Label("  ~> ")
        self.prompt_line["cmd"] = Gtk.Label("echo ")
        self.prompt_line["arg"] = Gtk.Label("\"nice\" ")

        line.pack_start(self.prompt_line["prompt"], False, True, 0)
        line.pack_start(self.prompt_line["cmd"], False, True, 0)
        line.pack_start(self.prompt_line["arg"], False, True, 0)

        return line

    def _create_preview_margin(self):
        area = Gtk.DrawingArea()
        area.set_size_request(270, 50)

        return area

    def update_preview(self, new_theme):
        self.modify_bg(0, color=Gdk.color_parse(new_theme['background_color']))
        self.update_palette_preview(new_theme['palette'])
        self.update_prompt_line_colors(new_theme['palette'])

    def update_palette_preview(self, palette):
        for i, color in enumerate(palette.split(":")[0:8]):
            self.palette_preview_colors[i].modify_bg(
                0, color=Gdk.color_parse(color))

    def update_prompt_line_colors(self, palette):
        palette = palette.split(":")
        self.prompt_line["prompt"].modify_fg(0,
                                             color=Gdk.color_parse(palette[6]))
        self.prompt_line["cmd"].modify_fg(0, color=Gdk.color_parse(palette[3]))
        self.prompt_line["arg"].modify_fg(0, color=Gdk.color_parse(palette[2]))
