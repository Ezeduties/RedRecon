from evidence.banner_engine import BannerEngine

engine = BannerEngine()

banner = engine.grab_banner(
    "10.0.9.5",
    21
)

print(banner)
