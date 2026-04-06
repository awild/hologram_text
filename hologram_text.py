import pya


# 4-column x 5-row bitmap font, rows top-to-bottom
FONT = {
    'A': [[0,1,1,0],
          [1,0,0,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],

    'B': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,0,1],
          [1,1,1,0]],

    'C': [[0,1,1,1],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [0,1,1,1]],

    'D': [[1,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,1,1,0]],

    'E': [[1,1,1,1],
          [1,0,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [1,1,1,1]],

    'F': [[1,1,1,1],
          [1,0,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [1,0,0,0]],

    'G': [[0,1,1,1],
          [1,0,0,0],
          [1,0,1,1],
          [1,0,0,1],
          [0,1,1,1]],

    'H': [[1,0,0,1],
          [1,0,0,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],

    'I': [[1,1,1,1],
          [0,1,1,0],
          [0,1,1,0],
          [0,1,1,0],
          [1,1,1,1]],

    'J': [[0,0,1,1],
          [0,0,0,1],
          [0,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],

    'K': [[1,0,0,1],
          [1,0,1,0],
          [1,1,0,0],
          [1,0,1,0],
          [1,0,0,1]],

    'L': [[1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [1,1,1,1]],

    'M': [[1,0,0,1],
          [1,1,1,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],

    'N': [[1,0,0,1],
          [1,1,0,1],
          [1,1,1,1],
          [1,0,1,1],
          [1,0,0,1]],

    'O': [[0,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],

    'P': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,0,0],
          [1,0,0,0]],

    'Q': [[0,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,1,0],
          [0,1,0,1]],

    'R': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,1,0],
          [1,0,0,1]],

    'S': [[0,1,1,1],
          [1,0,0,0],
          [0,1,1,0],
          [0,0,0,1],
          [1,1,1,0]],

    'T': [[1,1,1,1],
          [0,1,1,0],
          [0,1,1,0],
          [0,1,1,0],
          [0,1,1,0]],

    'U': [[1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],

    'V': [[1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0],
          [0,1,1,0]],

    'W': [[1,0,0,1],
          [1,0,0,1],
          [1,1,1,1],
          [1,1,1,1],
          [0,1,1,0]],

    'X': [[1,0,0,1],
          [1,0,0,1],
          [0,1,1,0],
          [1,0,0,1],
          [1,0,0,1]],

    'Y': [[1,0,0,1],
          [1,0,0,1],
          [0,1,1,0],
          [0,1,1,0],
          [0,1,1,0]],

    'Z': [[1,1,1,1],
          [0,0,0,1],
          [0,1,1,0],
          [1,0,0,0],
          [1,1,1,1]],

    '0': [[0,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],

    '1': [[0,1,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,0,0],
          [1,1,1,0]],

    '2': [[0,1,1,0],
          [1,0,0,1],
          [0,0,1,0],
          [0,1,0,0],
          [1,1,1,1]],

    '3': [[1,1,1,0],
          [0,0,0,1],
          [0,1,1,0],
          [0,0,0,1],
          [1,1,1,0]],

    '4': [[1,0,0,1],
          [1,0,0,1],
          [1,1,1,1],
          [0,0,0,1],
          [0,0,0,1]],

    '5': [[1,1,1,1],
          [1,0,0,0],
          [1,1,1,0],
          [0,0,0,1],
          [1,1,1,0]],

    '6': [[0,1,1,0],
          [1,0,0,0],
          [1,1,1,0],
          [1,0,0,1],
          [0,1,1,0]],

    '7': [[1,1,1,1],
          [0,0,0,1],
          [0,0,1,0],
          [0,1,0,0],
          [0,1,0,0]],

    '8': [[0,1,1,0],
          [1,0,0,1],
          [0,1,1,0],
          [1,0,0,1],
          [0,1,1,0]],

    '9': [[0,1,1,0],
          [1,0,0,1],
          [0,1,1,1],
          [0,0,0,1],
          [0,1,1,0]],

    '.': [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,1,0,0]],

    ',': [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,1,0,0],
          [1,0,0,0]],

    '!': [[0,1,1,0],
          [0,1,1,0],
          [0,1,1,0],
          [0,0,0,0],
          [0,1,1,0]],

    '?': [[0,1,1,0],
          [1,0,0,1],
          [0,0,1,0],
          [0,0,0,0],
          [0,0,1,0]],

    '-': [[0,0,0,0],
          [0,0,0,0],
          [1,1,1,1],
          [0,0,0,0],
          [0,0,0,0]],

    '+': [[0,0,0,0],
          [0,1,1,0],
          [1,1,1,1],
          [0,1,1,0],
          [0,0,0,0]],

    '=': [[0,0,0,0],
          [1,1,1,1],
          [0,0,0,0],
          [1,1,1,1],
          [0,0,0,0]],

    '/': [[0,0,0,1],
          [0,0,1,0],
          [0,1,1,0],
          [0,1,0,0],
          [1,0,0,0]],

    '(': [[0,0,1,0],
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0],
          [0,0,1,0]],

    ')': [[0,1,0,0],
          [0,0,1,0],
          [0,0,1,0],
          [0,0,1,0],
          [0,1,0,0]],

    ':': [[0,0,0,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,1,0,0],
          [0,0,0,0]],

    '_': [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [1,1,1,1]],

    ' ': [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]],
}


class HologramText(pya.PCellDeclarationHelper):

    def __init__(self):
        super(HologramText, self).__init__()
        self.param("text", self.TypeString, "Text", default="HELLO")
        self.param("text_height", self.TypeDouble, "Text Height (um)", default=10.0)
        self.param("line_width", self.TypeDouble, "Line Width (um)", default=0.5)
        self.param("line_spacing", self.TypeDouble, "Line Spacing (um)", default=0.5)
        self.param("layer", self.TypeLayer, "Layer", default=pya.LayerInfo(1, 0))

    def display_text_impl(self):
        return "HologramText: %s" % self.text

    def coerce_parameters_impl(self):
        if self.text_height <= 0:
            self.text_height = 10.0
        if self.line_width <= 0:
            self.line_width = 0.5
        if self.line_spacing < 0:
            self.line_spacing = 0.0

    def can_create_from_shape_impl(self):
        return False

    def transformation_from_shape_impl(self):
        return pya.Trans(pya.Point(0, 0))

    def produce_impl(self):
        dbu = self.layout.dbu

        # Vertical geometry: 5 rows of lines with 4 gaps between them
        # text_height = 5 * line_width + 4 * line_spacing
        # Row pitch = line_width + line_spacing
        row_pitch = self.line_width + self.line_spacing

        # Horizontal: each segment length equals row_pitch (square cells)
        seg_length = row_pitch
        seg_gap = self.line_spacing

        # Total character width = 4 segments + 3 gaps between segments
        char_width = 4 * seg_length + 3 * seg_gap
        char_gap = seg_length  # space between characters

        x_offset = 0.0

        for ch in self.text.upper():
            glyph = FONT.get(ch)
            if glyph is None:
                # Skip unknown characters
                continue

            for row_idx, row in enumerate(glyph):
                # Row 0 is the top row; y increases upward in layout
                y_bottom = (4 - row_idx) * row_pitch
                y_top = y_bottom + self.line_width

                for col_idx, pixel in enumerate(row):
                    if pixel:
                        x_left = x_offset + col_idx * (seg_length + seg_gap)
                        x_right = x_left + seg_length

                        box = pya.Box(
                            int(round(x_left / dbu)),
                            int(round(y_bottom / dbu)),
                            int(round(x_right / dbu)),
                            int(round(y_top / dbu)),
                        )
                        self.cell.shapes(self.layer_layer).insert(box)

            x_offset += char_width + char_gap


class HologramTextLib(pya.Library):

    def __init__(self):
        self.description = "Hologram Text PCell Library"
        self.layout().register_pcell("HologramText", HologramText())
        self.register("HologramTextLib")


# Instantiate the library when KLayout loads this file
HologramTextLib()
