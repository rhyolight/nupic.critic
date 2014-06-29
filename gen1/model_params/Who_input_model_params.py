MODEL_PARAMS = \
{ 'aggregationInfo': { 'days': 0,
                       'fields': [],
                       'hours': 0,
                       'microseconds': 0,
                       'milliseconds': 0,
                       'minutes': 0,
                       'months': 0,
                       'seconds': 0,
                       'weeks': 0,
                       'years': 0},
  'model': 'CLA',
  'modelParams': { 'anomalyParams': { u'anomalyCacheRecords': None,
                                      u'autoDetectThreshold': None,
                                      u'autoDetectWaitRecords': None},
                   'clParams': { 'alpha': 0.06951291702618762,
                                 'clVerbosity': 0,
                                 'regionName': 'CLAClassifierRegion',
                                 'steps': '1'},
                   'inferenceType': 'TemporalAnomaly',
                   'sensorParams': { 'encoders': { u'b0': { 'clipInput': True,
                                                            'fieldname': 'b0',
                                                            'maxval': 6000.0,
                                                            'minval': 0.0,
                                                            'n': 303,
                                                            'name': 'b0',
                                                            'type': 'ScalarEncoder',
                                                            'w': 21},
                                                   u'b1': None,
                                                   u'b2': None,
                                                   u'b3': { 'clipInput': True,
                                                            'fieldname': 'b3',
                                                            'maxval': 6000.0,
                                                            'minval': 0.0,
                                                            'n': 46,
                                                            'name': 'b3',
                                                            'type': 'ScalarEncoder',
                                                            'w': 21},
                                                   u'b4': None,
                                                   u'b5': None},
                                     'sensorAutoReset': None,
                                     'verbosity': 0},
                   'spEnable': True,
                   'spParams': { 'columnCount': 2048,
                                 'globalInhibition': 1,
                                 'inputWidth': 0,
                                 'maxBoost': 2.0,
                                 'numActiveColumnsPerInhArea': 40,
                                 'potentialPct': 0.8,
                                 'seed': 1956,
                                 'spVerbosity': 0,
                                 'spatialImp': 'cpp',
                                 'synPermActiveInc': 0.05,
                                 'synPermConnected': 0.1,
                                 'synPermInactiveDec': 0.04001537504049084},
                   'tpEnable': True,
                   'tpParams': { 'activationThreshold': 14,
                                 'cellsPerColumn': 32,
                                 'columnCount': 2048,
                                 'globalDecay': 0.0,
                                 'initialPerm': 0.21,
                                 'inputWidth': 2048,
                                 'maxAge': 0,
                                 'maxSegmentsPerCell': 128,
                                 'maxSynapsesPerSegment': 32,
                                 'minThreshold': 11,
                                 'newSynapseCount': 20,
                                 'outputType': 'normal',
                                 'pamLength': 4,
                                 'permanenceDec': 0.1,
                                 'permanenceInc': 0.1,
                                 'seed': 1960,
                                 'temporalImp': 'cpp',
                                 'verbosity': 0},
                   'trainSPNetOnlyIfRequested': False},
  'predictAheadTime': None,
  'version': 1}