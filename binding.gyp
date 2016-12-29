{
  'targets': [
    {
      'target_name': 'node_quickfix',
      'product_extension': 'node',
      'type': 'static_library',
      'sources': [
        'src/Threading.h',
        'src/Dispatcher.h',
      	'src/FixCredentials.h',
      	'src/FixEvent.h',
      	'src/FixMessageUtil.h',
      	'src/FixSession.h',
      	'src/FixSession.cpp',		    
      	'src/FixLogon.h',
      	'src/FixLoginProvider.h',
      	'src/FixLoginProvider.cpp',
      	'src/FixLoginResponse.h',
      	'src/FixLoginResponse.cpp',
      	'src/FixAcceptor.h',
      	'src/FixAcceptor.cpp',
      	'src/FixAcceptorStartWorker.h',
      	'src/FixAcceptorStartWorker.cpp',
      	'src/FixAcceptorStopWorker.h',
      	'src/FixAcceptorStopWorker.cpp',
      	'src/FixApplication.h',
      	'src/FixApplication.cpp',
      	'src/FixConnection.h',
      	'src/FixConnection.cpp',
      	'src/FixInitiator.h',
      	'src/FixInitiator.cpp',
      	'src/FixInitiatorStartWorker.h',
      	'src/FixInitiatorStartWorker.cpp',
      	'src/FixInitiatorStopWorker.h',
      	'src/FixInitiatorStopWorker.cpp',
      	'src/FixSendWorker.h',
      	'src/FixSendWorker.cpp',
		'src/node_quickfix.cpp'
      ],  	  
      'include_dirs': [
        "<!(node -e \"require('nan')\")"		
      ],		  
	  'direct_dependent_settings': {
        'include_dirs': ['src']
      }, 
	  'conditions': [
        ['OS=="win"', {          
          'variables': {
            'qf_include_dir%': '<!(IF DEFINED qf_INCLUDE_DIR (echo %qf_INCLUDE_DIR%) ELSE (echo C:\Users\thesl\include\quickfix))',
            'qf_lib_dir%': '<!(IF DEFINED qf_LIB_DIR (echo %qf_LIB_DIR%) ELSE (echo C:\Users\thesl\lib))',
            'qf_version%': '<!(IF DEFINED qf_VERSION (echo %qf_VERSION%) ELSE (echo 11))'
          },
          'link_settings': {'libraries': [ '-l<(qf_lib_dir)\quickfix.lib','-l<(qf_lib_dir)\ws2_32ws2_32.lib' ] }
        }]
      ]
    }
  ]
}
