
#  
use strict;use LWP::UserAgent;use HTTP::Request;use HTTP::Headers;
my $objUserAgent = LWP::UserAgent->new;
my $objHeader = HTTP::Headers->new;

	# stop seeding now
	my $uripath = "http://localhost:11020/services/dist/cancel/" . $ARGV[0];
	my $request = '{"comment": "test cancel" }';
	
	my $objRequest = HTTP::Request->new("POST", $uripath, $objHeader, $request);
	
	my $objResponse = $objUserAgent->request($objRequest);
	if ($objResponse->is_error)
	{
    	print ("ERROR \n");
    	print $objResponse->status_line;
    	print $objResponse->content();

	    print ("\n");
	}
	else
	{
	    print $objResponse->content();
	    print ("\n");
	}
	print 'stopped thread with uuid ' . $ARGV[0];