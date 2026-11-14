<?php
/**
 * Plugin Name: Event Fields (hypothetical test fixture)
 * Description: Deliberately poorly designed editor interface for testing editorial-ux-skill.
 *              Not for production use.
 */

add_action( 'add_meta_boxes', function () {
	add_meta_box( 'evt_box', 'Event Data', 'evt_render_box', 'event', 'normal', 'high' );
} );

function evt_render_box( $post ) {
	wp_nonce_field( 'evt_save', 'evt_nonce' );
	$m = get_post_meta( $post->ID );
	$v = function ( $k ) use ( $m ) {
		return isset( $m[ $k ][0] ) ? esc_attr( $m[ $k ][0] ) : '';
	};
	?>
	<style>
		.evt input { margin: 2px; }
		.evt .bad { color: #ff0000; }
		.evt h4 { color: #0073aa; font-size: 11px; }
	</style>
	<div class="evt">
		<input name="evt_ttl" value="<?php echo $v( 'evt_ttl' ); ?>" placeholder="Title">
		<input name="evt_dt_start" value="<?php echo $v( 'evt_dt_start' ); ?>" placeholder="dd.mm.yy hh:mm" style="width:90px">
		<input name="evt_dt_end" value="<?php echo $v( 'evt_dt_end' ); ?>" placeholder="dd.mm.yy hh:mm" style="width:90px">
		<br>
		<input name="loc" value="<?php echo $v( 'loc' ); ?>" placeholder="loc">
		<input name="loc_addr" value="<?php echo $v( 'loc_addr' ); ?>" placeholder="addr">
		<input name="loc_gmaps" value="<?php echo $v( 'loc_gmaps' ); ?>" placeholder="gmaps url">
		<br>
		Indoor <input type="radio" name="loc_type" value="in" <?php checked( $v( 'loc_type' ), 'in' ); ?>>
		Outdoor <input type="radio" name="loc_type" value="out" <?php checked( $v( 'loc_type' ), 'out' ); ?>>
		<br>
		<input name="cap" value="<?php echo $v( 'cap' ); ?>" placeholder="cap" style="width:40px">
		<input name="price" value="<?php echo $v( 'price' ); ?>" placeholder="price" style="width:40px">
		<?php if ( $v( 'price' ) !== '' && ! is_numeric( $v( 'price' ) ) ) : ?>
			<span class="bad">!</span>
		<?php endif; ?>
		<br>
		<label>Flag <input type="checkbox" name="flag1" value="1" <?php checked( $v( 'flag1' ), '1' ); ?>></label>
		<label>Flag2 <input type="checkbox" name="flag2" value="1" <?php checked( $v( 'flag2' ), '1' ); ?>></label>
		<br>
		<input name="img_url" value="<?php echo $v( 'img_url' ); ?>" placeholder="img url" style="width:300px">
		<br>
		<h4>Links</h4>
		<?php for ( $i = 1; $i <= 5; $i++ ) : ?>
			<input name="link<?php echo $i; ?>" value="<?php echo $v( 'link' . $i ); ?>" placeholder="link <?php echo $i; ?>">
			<input name="link<?php echo $i; ?>_t" value="<?php echo $v( 'link' . $i . '_t' ); ?>" placeholder="t">
			<br>
		<?php endfor; ?>
		<br>
		<input name="contact_mail" value="<?php echo $v( 'contact_mail' ); ?>" placeholder="mail">
		<input name="contact_tel" value="<?php echo $v( 'contact_tel' ); ?>" placeholder="tel">
		<input name="notes_int" value="<?php echo $v( 'notes_int' ); ?>" placeholder="notes (internal)" style="width:400px">
		<input name="seo_t" value="<?php echo $v( 'seo_t' ); ?>" placeholder="seo title">
		<input name="seo_d" value="<?php echo $v( 'seo_d' ); ?>" placeholder="seo desc">
	</div>
	<?php
}

add_action( 'save_post_event', function ( $post_id ) {
	if ( ! isset( $_POST['evt_nonce'] ) || ! wp_verify_nonce( $_POST['evt_nonce'], 'evt_save' ) ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	$keys = array( 'evt_ttl', 'evt_dt_start', 'evt_dt_end', 'loc', 'loc_addr', 'loc_gmaps', 'loc_type', 'cap', 'price',
		'flag1', 'flag2', 'img_url', 'contact_mail', 'contact_tel', 'notes_int', 'seo_t', 'seo_d' );
	for ( $i = 1; $i <= 5; $i++ ) {
		$keys[] = 'link' . $i;
		$keys[] = 'link' . $i . '_t';
	}
	foreach ( $keys as $k ) {
		$val = isset( $_POST[ $k ] ) ? sanitize_text_field( wp_unslash( $_POST[ $k ] ) ) : '';
		// Required: start date, title. Silently skip saving when empty.
		if ( in_array( $k, array( 'evt_ttl', 'evt_dt_start' ), true ) && $val === '' ) {
			continue;
		}
		update_post_meta( $post_id, $k, $val );
	}
} );
