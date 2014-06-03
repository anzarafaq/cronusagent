
#  
use strict;use LWP::UserAgent;use HTTP::Request;use HTTP::Headers;
my $objUserAgent = LWP::UserAgent->new;
my $objHeader = HTTP::Headers->new;
#$objHeader->push_header('X-EBAY-API-COMPATIBILITY-LEVEL' => '311');



#my $request = '{"package": "http://qa-cloudesvc02.qa.ebay.com/ebox-1.0.0.win.cronus", "packageloc":"ebox-1.0.0.win.cronus"}';
#my $request = '{"package": "http://qa-cloudesvc02.qa.ebay.com/E705_CORE_BUNDLED_12652435_R1.ZIP", "packageloc":"E705_CORE_BUNDLED_12652435_R1.ZIP"}';
my $request = '{"package": "http://qa-cloudesvc02.qa.ebay.com/ebox-1.0.0.win.cronus.torrent", "packageloc":"ebox-1.0.0.win.cronus"}';
#my $request = '{"package": "http://qa-cloudesvc02.qa.ebay.com/E705_CORE_BUNDLED_12652435_R1.ZIP.torrent", "packageloc":"E705_CORE_BUNDLED_12652435_R1.zip"}';

my $uripath = "http://localhost:11020/services/dist/startdownload";


my $objRequest = HTTP::Request->new("POST", $uripath, $objHeader, $request);   

print $objRequest->content();

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

my $status = $objResponse->content();

sleep(1);

if($status =~ m/\/status\/(.*?)\"/) {
	
        print ('uuid is ' . $1);
        print ("\n");
        my $uripath = "http://localhost:11020/status/" . $1; 
        print $uripath;
        print ("\n");

	my $objRequest1 = HTTP::Request->new("GET", $uripath, $objHeader, "");   

	for (my $count = 1; $count < 500; $count++) {

		my $objResponse1 = $objUserAgent->request($objRequest1);
		print $count;
		print " : ";
        	my $res = $objResponse1->content();
        	print $res;
        	
        	my $progress = $res;
		        	
		if($progress =~ m/progress\":(.*?)}/) {
		    my $intProgress = int($1);
		    if ($intProgress == 100) {
		       print ("\n\ntotal time is: ");
		       print $count;
		       print (" seconds! \n");
		       last;
		    }
        	}
        	
		print ("\n");
		sleep(1);
	}
}