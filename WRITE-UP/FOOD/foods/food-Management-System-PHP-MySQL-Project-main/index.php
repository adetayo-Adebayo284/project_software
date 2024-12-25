<?php
    include("includes/header.php");
    include("includes/connection.php");
    include("functions/index_process.php");
    include("functions/notification.php");

    display_notification_messages();
    display_notification_messages_sucesses();
?>
<style>
    .site-menu{
			position: absolute;
			top: 50%;
			left: 50%;
			-webkit-transform: translate(-50%);
			transform: translate(-50%, -500%);
			z-index: 2;
			font-family: 'Montserrat', sans-serif;
		}
		.site-menu a{
			border: 1px solid #000;
    		border-radius: 15px;
    		padding: 12px 35px;
    		margin: 0 5px;
    		outline: none;
    		color: #000;
    		font-size: 2rem;
    		font-weight: 600;
    		line-height: 1.4;
    		text-align: center;
    		text-decoration: none;
    		transition: 0.2s;
		}
		.site-menu a:hover{
			border: 1px solid #ff105f;
			outline: none;
			color: #ffffff;
			background: linear-gradient(to left, #ff105f, #ffad06);
			box-shadow: 0 0 30px #ff105f, 0 0 60px #ffad06;
			text-decoration: none;
		}
</style>
            <main>
                
                <!-- <section class="py-5 text-center container">
                    <div class="row py-lg-5">
                        <div class="col-lg-6 col-md-8 mx-auto">
                            <h1 class="fw-light">Bookstore</h1>
                            <p class="lead text-body-secondary">A Bookstore Management System aims to eliminate paperwork and streamline book-related tasks. It centralizes all activities and allows for multi-tasking. Records are kept securely, and the system prioritizes user experience. Continuous improvement is a priority.</p>
                        </div>
                    </div>
                </section> -->
                <section>
                    <div class="site-menu">
                        <a href="book_list.php" >MENU</a>
                   
                    </div>
                </section>
                <br><br>
                
                <div class="album py-5 bg-body-tertiary">
                    <div class="container">
                        <div class="row">
                            <?php while ($row = mysqli_fetch_assoc($result)) { ?>
                                <div class="col-md-4">
                                    <a class="link-offset-2 link-underline link-underline-opacity-0" href="book_detail.php?id=<?php echo $row['book_id']; ?>">
                                        <div class="card shadow-sm">
                                            <img class="bd-placeholder-img card-img-top" width="100" height="500" src="<?php echo $row['book_img']; ?>">
                                            <div class="card-body">
                                                <div class="d-flex justify-content-between align-items-center">
                                                    <small class="text-body-secondary"><?php echo $row['book_name']; ?></small>
                                                    <small class="text-body-secondary">₸ <?php echo $row['book_price']; ?></small>
                                                </div>
                                            </div>
                                        </div>
                                    </a>
                                </div>
                            <?php } ?>
                        </div>
                    </div>
                </div>
                
            </main>

<?php
    include("includes/footer.php");
?>
