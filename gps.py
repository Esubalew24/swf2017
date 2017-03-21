from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from kivy.garden.mapview import MapMarker

kv = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: app.gps_location
    Label:
        text: app.gps_status
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        padding: '4dp'
        ToggleButton:
            text: 'Start' if self.state == 'normal' else 'Stop'
            on_state:
                app.start(1000, 0) if self.state == 'down' else \
                app.stop()
'''

class GpsMarker(MapMarker):

    def update_position(self):
        """
        Updates marker position on map layer.
        """
        layer = self._layer
        if layer is None:
            return
        mapview = layer.parent
        marker = self
        layer.set_marker_position(mapview, marker)

    def on_lat(self, instance, value):
        self.update_position()

    def on_lon(self, instance, value):
        self.update_position()


class GpsTest(App):
    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
                                          '{}={}'.format(k, v) for k, v in kwargs.items()])

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass


if __name__ == '__main__':
    GpsTest().run()


