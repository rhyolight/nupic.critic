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
                   'clParams': { 'alpha': 0.010625249451786521,
                                 'clVerbosity': 0,
                                 'regionName': 'CLAClassifierRegion',
                                 'steps': '1'},
                   'inferenceType': 'TemporalAnomaly',
                   'sensorParams': { 'encoders': { u'b0': None,
                                                   u'b1': None,
                                                   u'b2': { 'clipInput': True,
                                                            'fieldname': 'b2',
                                                            'maxval': 6000.0,
                                                            'minval': 0.0,
                                                            'n': 88,
                                                            'name': 'b2',
                                                            'type': 'ScalarEncoder',
                                                            'w': 21},
                                                   u'b3': None,
                                                   u'b4': None,
                                                   u'b5': None,
                                                   u'b6': None,
                                                   u'b7': None,
                                                   u'b8': None,
                                                   u'b9': { 'clipInput': True,
                                                            'fieldname': 'b9',
                                                            'maxval': 6000.0,
                                                            'minval': 0.0,
                                                            'n': 109,
                                                            'name': 'b9',
                                                            'type': 'ScalarEncoder',
                                                            'w': 21}},
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
                                 'synPermInactiveDec': 0.1},
                   'tpEnable': True,
                   'tpParams': { 'activationThreshold': 13,
                                 'cellsPerColumn': 32,
                                 'columnCount': 2048,
                                 'globalDecay': 0.0,
                                 'initialPerm': 0.21,
                                 'inputWidth': 2048,
                                 'maxAge': 0,
                                 'maxSegmentsPerCell': 128,
                                 'maxSynapsesPerSegment': 32,
                                 'minThreshold': 9,
                                 'newSynapseCount': 20,
                                 'outputType': 'normal',
                                 'pamLength': 2,
                                 'permanenceDec': 0.1,
                                 'permanenceInc': 0.1,
                                 'seed': 1960,
                                 'temporalImp': 'cpp',
                                 'verbosity': 0},
                   'trainSPNetOnlyIfRequested': False},
  'predictAheadTime': None,
  'version': 1}