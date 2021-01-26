import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 12, 41623])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDG1tQ0lGSGVhZGVyc3EIXXEJTmFVDGFyb21hdGljTW9kZXEKSwFLAX2HVQp2ZHdEZW5zaXR5cQtLAUdAFAAAAAAAAH2HVQZoaWRkZW5xDEsBiX2HVQ1hcm9tYXRpY0NvbG9ycQ1LAU59h1UPcmliYm9uU21vb3RoaW5ncQ5LAUsAfYdVCWF1dG9jaGFpbnEPSwGIfYdVCnBkYlZlcnNpb25xEEsBSwB9h1UIb3B0aW9uYWxxEX1xEihVC2NoYXJnZU1vZGVscROIiUsBVQxVU0VSX0NIQVJHRVNxFH2Hh1UIb3BlbmVkQXNxFYiJSwEoVQ1tb2wyOkhFTS5tb2wycRZOTksBdHEXfYeHVQhtb2wybmFtZXEYiIlLAVUHSEVNLUlDNnEZfYeHVQhtb2wydHlwZXEaiIlLAVUFU01BTExxG32Hh3VVD2xvd2VyQ2FzZUNoYWluc3EcSwGJfYdVCWxpbmVXaWR0aHEdSwFHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcR5LAUsAfYdVBG5hbWVxH0sBWAcAAABIRU0tSUM2fYdVD2Fyb21hdGljRGlzcGxheXEgSwGJfYdVD3JpYmJvblN0aWZmbmVzc3EhSwFHP+mZmZmZmZp9h1UKcGRiSGVhZGVyc3EiXXEjfXEkYVUDaWRzcSVLAUsASwCGfYdVDnN1cmZhY2VPcGFjaXR5cSZLAUe/8AAAAAAAAH2HVRBhcm9tYXRpY0xpbmVUeXBlcSdLAUsCfYdVFHJpYmJvbkhpZGVzTWFpbmNoYWlucShLAYh9h1UHZGlzcGxheXEpSwGIfYd1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksBVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAYl9h1UEbmFtZXEESwFYAwAAAEhFTX2HVQVjaGFpbnEFSwFYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksBSwJ9h1UCc3NxB0sBiYmGfYdVCG1vbGVjdWxlcQhLAUsAfYdVC3JpYmJvbkNvbG9ycQlLAU59h1UFbGFiZWxxCksBWAAAAAB9h1UKbGFiZWxDb2xvcnELSwFOfYdVCGZpbGxNb2RlcQxLAUsBfYdVBWlzSGV0cQ1LAYl9h1ULbGFiZWxPZmZzZXRxDksBTn2HVQhwb3NpdGlvbnEPXXEQSwFLAYZxEWFVDXJpYmJvbkRpc3BsYXlxEksBiX2HVQhvcHRpb25hbHETfVUEc3NJZHEUSwFK/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECSzdOfYdVBWF0b21zcQNdcQQoXXEFKEsCSwNlXXEGKEsCSwRlXXEHKEsDSwVlXXEIKEsDSxtlXXEJKEsESwZlXXEKKEsESwdlXXELKEsFSwZlXXEMKEsFSy1lXXENKEsHSwhlXXEOKEsOSw9lXXEPKEsOSxBlXXEQKEsQSxFlXXERKEsQSxNlXXESKEsRSxRlXXETKEsRSzllXXEUKEsSSxNlXXEVKEsSSxRlXXEWKEsSSxVlXXEXKEsUSzVlXXEYKEsVSxZlXXEZKEsbSxxlXXEaKEsfSyBlXXEbKEshSyJlXXEcKEshSyNlXXEdKEskSyVlXXEeKEsmSydlXXEfKEsmSyhlXXEgKEspSyplXXEhKEspSytlXXEiKEspSyxlXXEjKEstSy5lXXEkKEstSy9lXXElKEstSzBlXXEmKEsxSzJlXXEnKEsxSzNlXXEoKEsxSzRlXXEpKEs1SzZlXXEqKEs1SzdlXXErKEs1SzhlXXEsKEs5SzplXXEtKEs5SztlXXEuKEs5Sz9lXXEvKEs8Sz1lXXEwKEs8Sz5lXXExKEs8S0JlXXEyKEs/S0BlXXEzKEs/S0FlXXE0KEs/S0ZlXXE1KEtCS0NlXXE2KEtCS0RlXXE3KEtCS0VlXXE4KEtFS0hlXXE5KEtFS0plXXE6KEtGS0dlXXE7KEtGS0llZVUFbGFiZWxxPEs3WAAAAAB9h1UIaGFsZmJvbmRxPUs3iH2HVQZyYWRpdXNxPks3Rz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cT9LN059h1UIZHJhd01vZGVxQEs3SwF9h1UIb3B0aW9uYWxxQX1xQlUIbW9sMnR5cGVxQ4iJSzdVATF9h4dzVQdkaXNwbGF5cURLN0sCfYd1Lg=='))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'),
u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'),
u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'),
u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'),
u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'),
u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'coordination complexes of HEM-IC6 (#0)', u'distance monitor'], 'bondInfo': [{'color': (25, None, {}), 'atoms': [[11, 14], [11, 10], [11, 12], [36, 6], [36, 38], [29, 10], [29, 2], [29, 25], [29, 19], [13, 49], [13, 12], [13, 9], [25, 26], [25, 23], [26, 27], [26, 30], [33, 31], [9, 7], [9, 10], [24, 23], [24, 30], [24, 41], [12, 60], [23, 21], [30, 31]], 'label': (25, u'', {}), 'halfbond': (25, False, {}), 'labelColor': (25, None, {}), 'labelOffset': (25, chimera.Vector(-1e+99, 0.0, 0.0), {chimera.Vector(-1e+99, 0.0, 0.0): [11], chimera.Vector(-1e+99, 0.0, 0.0): [1], chimera.Vector(-1e+99, 0.0, 0.0): [23], chimera.Vector(-1e+99, 0.0, 0.0): [10], chimera.Vector(-1e+99, 0.0, 0.0): [9], chimera.Vector(-1e+99, 0.0, 0.0): [24], chimera.Vector(-1e+99, 0.0, 0.0): [20], chimera.Vector(-1e+99, 0.0, 0.0): [14], chimera.Vector(-1e+99, 0.0, 0.0): [21], chimera.Vector(-1e+99, 0.0, 0.0): [22], chimera.Vector(-1e+99, 0.0, 0.0): [13], chimera.Vector(-1e+99, 0.0, 0.0): [7], chimera.Vector(-1e+99, 0.0, 0.0): [8], chimera.Vector(-1e+99, 0.0, 0.0): [15], chimera.Vector(-1e+99, 0.0, 0.0): [16], chimera.Vector(-1e+99, 0.0, 0.0): [17], chimera.Vector(-1e+99, 0.0, 0.0): [4], chimera.Vector(-1e+99, 0.0, 0.0): [18], chimera.Vector(-1e+99, 0.0, 0.0): [19], chimera.Vector(-1e+99, 0.0, 0.0): [5], chimera.Vector(-1e+99, 0.0, 0.0): [12], chimera.Vector(-1e+99, 0.0, 0.0): [2], chimera.Vector(-1e+99, 0.0, 0.0): [6], chimera.Vector(-1e+99, 0.0, 0.0): [3]}),
'drawMode': (25, 0, {}), 'display': (25, 2, {})}, {'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (2, 2, {}), 'color': (2, 6, {7: [1]}), 'optional': {'fixedLabels': (True, False, (2, None, {False: [1]}))}, 'display': (2, True, {}), 'showStubBonds': (2, False, {}), 'lineWidth': (2, 1, {2: [0]}), 'stickScale': (2, 1, {}), 'id': [0, -2]}
	modelAssociations = {0: [155]}
	colorInfo = (9, (u'green', (0, 1, 0, 1)), {(u'Fe', (0.878431, 0.4, 0.2, 1)): [4], (u'medium purple', (0.576471, 0.439216, 0.858824, 1)): [6], (u'Cd', (1, 0.85098, 0.560784, 1)): [2], (u'magenta', (1, 0, 1, 1)): [1], (u'O', (1, 0.0509804, 0.0509804, 1)): [5], (u'Nd', (0.780392, 1, 0.780392, 1)): [3], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [7]})
	viewerInfo = {'cameraAttrs': {'center': (0.88849999761581, -0.055, -0.8215), 'fieldOfView': 25, 'nearFar': (10.2299999547, -11.8729999547), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -0.8215}, 'viewerAttrs': {'viewSize': 11.0514999547, 'highlight': 0, 'clipping': False, 'labelsOnTop': True, 'scaleFactor': 1}, 'viewerHL': 8, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': None}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [ ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 1 }
	windowSize = (1024, 1024)
	xformMap = {0: (((0, 0, 1), 0), (0, 0, 0), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 155: True, 156: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

